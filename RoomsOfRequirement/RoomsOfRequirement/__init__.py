import sqlite3
import re
from sqlite3 import Error
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import *

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_table(conn, create_table_sql, table_name):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS ''' + table_name + ';')
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def formatTime(time):
    # split the time into start time and end time
    time_split = time.split('-')

    startTime = time_split[0]
    endTime = time_split[1]

    # get the time into the rigth format to change int0 24hr
    if ':' not in startTime:
        startTime = startTime + ':00'

    # add AM and PM to start time and end end time
    if endTime[-2:] == "AM":
        startTime = startTime + ' AM'
        endTime = endTime[:-2] + ' AM'
    else:
        # special case for 12 AM
        if(startTime >= '10:00' and startTime < '12:00'):
            startTime = startTime + ' AM'
        else:
            startTime = startTime + ' PM'
        endTime = endTime[:-2] + ' PM'

    # convert the time into 24hr format
    startTime = datetime.strptime(startTime, '%I:%M %p')
    startTime = startTime.strftime("%H:%M %p")
    startTime = startTime[:-3]

    endTime = datetime.strptime(endTime, '%I:%M %p')
    endTime = endTime.strftime("%H:%M %p")
    endTime = endTime[:-3]

    return (startTime, endTime)

def insert_classroom_data(conn, url, ID_constant):
    #This class is used to scrape all the classes listed under one subject
    #Example URL to scrape:
    #http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/ACCT.html

    data = [] #List used to hold all the data scraped from the html
    pageToParse = urlopen(url)
    parsedPage = BeautifulSoup(pageToParse, "html.parser")
    for element in parsedPage.find_all('td'): #gets every element that has the 'td' tag
        data.append(element.text)  #add that element to the data list
        element.next_sibling

    cur = conn.cursor()
    ID = ID_constant * 10000 # give each class section a unique ID
    i = 5  # The first entry is at 5, there is a new class every 11 entries

    while i < len(data) - 3:
        fields = (data[i], data[i+1], data[i+3])  # Day, time, class respectively
        # Classes labeled 'TBA' or 'Online-Only' are ignored
        if len(fields[2]) > 8 or fields[2] == 'TBA' or fields[1] == 'TBA':
            pass
        else:

            # initialize required data for insert
            day = fields[0]

            # convert time to usuable 24hr format
            time_formatted = formatTime(fields[1])
            start_time = time_formatted[0]
            end_time = time_formatted[1]

            classroom = fields[2]

            # create a tuple of data for inserting
            classroom_row = (ID, classroom, start_time, end_time)

            #inserting sql
            insert_classroom_table = '''INSERT INTO CLASSROOM (
                                        class_id,
                                        classroom,
                                        start_time,
                                        end_time)
                                        VALUES (?,?,?,?)'''

            insert_weekday_table = '''INSERT INTO WEEKDAY (
                                      class_id,
                                      weekday)
                                      VALUES (?,?)'''

            cur.execute(insert_classroom_table, classroom_row)

            #split weekdays based on capitalization
            #ie MW become [M,W]
            weekdays = re.findall('[A-Z][^A-Z]*', day)
            for weekday in weekdays:
                cur.execute(insert_weekday_table, (ID, weekday))
            ID = ID + 1
        i += 11

def webcrawler(conn):
    data = [] #List used to hold all the data scraped from the html
    home_url = 'http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/'
    pageToParse = urlopen(home_url)

    parsedPage = BeautifulSoup(pageToParse, "html.parser")
    for element in parsedPage.find_all(href = True): #gets every element that has the 'td' tag
        data.append(element.text)  #add that element to the data list
        element.next_sibling
    r = re.compile('.*\(')
    #r = re.compile(".*Human")
    newList = list(filter(r.match, data))
    constant = 0
    for data in newList:
        html_extender = data[data.find('(') + 1:-1].replace(' ', 'z')
        html_extender = html_extender.replace('/', 'x')
        insert_classroom_data(conn, home_url + html_extender + '.html', constant)
        constant = constant + 1

def main():
    database = 'db.sqlite3'

    create_classroom_table = '''CREATE TABLE CLASSROOM (
                                class_id integer PRIMARY KEY,
                                classroom text,
                                start_time text,
                                end_time text
    );'''

    create_weekday_table = '''CREATE TABLE WEEKDAY (
                              class_id integer,
                              weekday text,
                              PRIMARY KEY(class_id, weekday),
                              FOREIGN KEY (class_id)
                              REFERENCES CLASSROOM (class_id)
    );'''
    # create a database connection
    conn = create_connection(database)

    weekday_ref = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']

    current_weekday = weekday_ref[datetime.today().weekday()]

    current_hour = datetime.today().strftime("%H:%M")


    if conn is not None:
        # create table
        create_table(conn, create_classroom_table, 'classroom');
        create_table(conn, create_weekday_table, 'weekday');

        webcrawler(conn);

        conn.commit()

        conn.close()
    else:
        print("Error! cannot create the database connection.")

main()
