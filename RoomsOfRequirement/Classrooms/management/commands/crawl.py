""" this is a script that takes the html data from the CSULB catalog and adds the list of classes
    into the database
    To run it, use the command `python manage.py crawl` while inside the virtualenv.
"""
import sqlite3
import re
from urllib.request import urlopen
from datetime import datetime
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Required to use as a custom Django command"""
    help = 'Updates the database with currently available classes.'

    def handle(self, *args, **kargs):
        main()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as err:
        print(err)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except sqlite3.Error as err:
        print(err)


def format_time(start_end):
    """ format time into a format our database can understand
    :param time: string representing time taken from the web scraper
    :return: tuple representing the start and end times individually formatted
    """
    # split the time into start time and end time
    time_split = start_end.split('-')

    start_time = time_split[0]
    end_time = time_split[1]

    # get the time into the rigth format to change int0 24hr
    if ':' not in start_time:
        start_time = start_time + ':00'

    # add AM and PM to start time and end end time
    if end_time[-2:] == 'AM':
        start_time = start_time + ' AM'
        end_time = end_time[:-2] + ' AM'
    else:
        # special case for 12 AM
        if '10:00' <= start_time < '12:00':
            start_time = start_time + ' AM'
        else:
            start_time = start_time + ' PM'
        end_time = end_time[:-2] + ' PM'

    # convert the time into 24hr format
    start_time = datetime.strptime(start_time, '%I:%M %p')
    start_time = start_time.strftime('%H:%M %p')
    start_time = start_time[:-3]

    end_time = datetime.strptime(end_time, '%I:%M %p')
    end_time = end_time.strftime('%H:%M %p')
    end_time = end_time[:-3]

    return (start_time, end_time)


def parse_and_insert_classroom_data(conn, url, id_constant):
    """ Scrapes all the classes listed under one subject
    :param conn: Connection object
    :param url: The url we connect to in order to gather data
    :param id_constant: incremented constant that gives each class a unique id
    :return:
    """
    # Example URL to scrape:
    # http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/ACCT.html

    data = []  # List used to hold all the data scraped from the html
    parsed_page = BeautifulSoup(urlopen(url), 'html.parser')
    # gets every element that has the 'td' tag
    for element in parsed_page.find_all('td'):
        data.append(element.text)  # add that element to the data list

    cur = conn.cursor()
    class_id = id_constant * 10000  # give each class section a unique ID
    i = 5  # The first entry is at 5, there is a new class every 11 entries

    while i < len(data) - 3:
        # Day, time, class respectively
        fields = (data[i], data[i+1], data[i+3])
        # Classes labeled 'TBA' or 'Online-Only' are ignored
        if len(fields[2]) > 8 or fields[2] == 'TBA' or fields[1] == 'TBA':
            pass
        else:
            insert_classroom_data(cur, fields, class_id)
            class_id = class_id + 10
        i += 11


def insert_classroom_data(cur, fields, class_id):
    """ Inserts the classroom field into the database
    :param cur: Connection cursor
    :param fields: The tuple of class data taken from the HMTL
    :param class_id: Multiplied constant that gives each class a unique id
    :return:
    """
    # initialize required data for insert
    day, start_end, classroom = fields

    # convert time to usuable 24hr format
    start_time, end_time = format_time(start_end)

    # inserting sql
    insert_classroom_table = (
        'INSERT INTO CLASSROOM ('
        'class_id,'
        'classroom,'
        'weekday,'
        'start_time,'
        'end_time)'
        'VALUES (?,?,?,?,?)'
    )

    # split weekdays based on capitalization
    # ie MW become [M,W]
    weekdays = re.findall('[A-Z][^A-Z]*', day)
    for weekday in weekdays:
        cur.execute(insert_classroom_table,
                    (class_id, classroom, weekday, start_time, end_time))
        class_id += 1


def webcrawler(conn):
    """ Gets all the href tags from the url then performs the database load
    :param conn: Connection object
    :return:
    """
    data = []  # List used to hold all the data scraped from the html
    home_url = ('http://web.csulb.edu/depts/enrollment/registration/class_schedule/'
                'Spring_2019/By_Subject/')
    page_to_parse = urlopen(home_url)

    parsed_page = BeautifulSoup(page_to_parse, 'html.parser')
    # gets every element that has the 'td' tag
    for element in parsed_page.find_all(href=True):
        data.append(element.text)  # add that element to the data list

    regex = re.compile('.*\\(')
    #regex = re.compile('.*Human')
    subjects = list(filter(regex.match, data))
    constant = 0
    for subject in subjects:
        # Get the shorthand subject name from each subject
        # Note, URLs don't contain spaces so some subjects have the space replaced with 'z's
        subj = subject[subject.find('(') + 1:-1].replace(' ', 'z')
        subj = subj.replace('/', 'x')
        print('Inserting class data for {}'.format(subj))
        parse_and_insert_classroom_data(
            conn, home_url + subj + '.html', constant)
        constant = constant + 1


def find_empty_classroom(conn, current_weekday, current_hour):
    """ Finds empty classrooms
    :param conn: Connection object
    :param current_weekday
    :param current_hour
    :return: List of classrooms that are current not in use
    """
    cur = conn.cursor()

    sql = (
        'SELECT DISTINCT classroom FROM classroom '
        'EXCEPT '
        'SELECT classroom FROM classroom NATURAL JOIN weekday '
        'WHERE weekday = ? AND (start_time < ? and end_time > ?)'
    )
    cur.execute(sql, (current_weekday, current_hour, current_hour))

    return cur.fetchall()


def select_data(conn, sql):
    """ Uses the database to execute a sql command and return a result
    :param conn: Connection object
    :param sql: SQL query
    :return: Result list from the SQL query
    """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def main():
    """ Entry point """
    database = 'db.sqlite3'

    create_classroom_table = (
        'CREATE TABLE IF NOT EXISTS CLASSROOM ('
        'class_id integer PRIMARY KEY,'
        'classroom text,'
        'weekday text,'
        'start_time text,'
        'end_time text'
        ');'
    )
    # create a database connection
    conn = create_connection(database)

    weekday_ref = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']

    current_weekday = weekday_ref[datetime.today().weekday()]

    current_hour = datetime.today().strftime('%H:%M')

    print(current_weekday)

    print(current_hour)
    if conn is not None:
        # create table
        create_table(conn, create_classroom_table)  # classroom

        if not select_data(conn, 'SELECT DISTINCT classroom from classroom'):
            begin = datetime.now()
            webcrawler(conn)
            diff = datetime.now() - begin
            print('Successfully processed entries in {}'.format(diff))
        else:
            print('Database already filled')

        # empty_classroom = find_empty_classroom(
        #    conn, current_weekday, current_hour)

        # for room in empty_classroom:
        #    print(room[0], end='  ')

        conn.commit()

        conn.close()
    else:
        print('Error! cannot create the database connection.')


if __name__ == '__main__':
    main()
