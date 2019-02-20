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

def select_all(conn, table_name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table_name)

    rows = cur.fetchall()

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

def get_weekday(conn):
    """ get weekday of current day
    :param conn: Connection object
    :return: int  0-6 (Sunday - Saturday)
    """
    # get weekday
    cur = conn.cursor()
    cur.execute('''SELECT strftime('%w','now')''')

    #return 0-6 Sunday - Saturday
    rows = cur.fetchall()

    return rows[0][0]

def formatTime(time):
    time_split = time.split('-')

    startTime = time_split[0]
    endTime = time_split[1]

    if ':' not in startTime:
        startTime = startTime + ':00'

    if endTime[-2:] == "AM":
        startTime = startTime + ' AM'
        endTime = endTime[:-2] + ' AM'
    else:
        if(startTime >= '10:00' and startTime < '12:00'):
            startTime = startTime + ' AM'
        else:
            startTime = startTime + ' PM'
        endTime = endTime[:-2] + ' PM'


    startTime = datetime.strptime(startTime, '%I:%M %p')
    startTime = startTime.strftime("%H:%M %p")
    startTime = startTime[:-3]

    endTime = datetime.strptime(endTime, '%I:%M %p')
    endTime = endTime.strftime("%H:%M %p")
    endTime = endTime[:-3]

    return (startTime, endTime)

def insert_classroom_data(conn):
    #This class is used to scrape all the classes listed under one subject
    #Example URL to scrape:
    #http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/ACCT.html

    data = [] #List used to hold all the data scraped from the html
    pageToParse = urlopen(
        'http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/CECS.html')

    parsedPage = BeautifulSoup(pageToParse, "html.parser")
    for element in parsedPage.find_all('td'): #gets every element that has the 'td' tag
        data.append(element.text)  #add that element to the data list
        element.next_sibling

    cur = conn.cursor()
    ID = 0
    i = 5  # The first entry is at 5, there is a new class every 11 entries
    while i < len(data):
        fields = (data[i], data[i+1], data[i+3])  # Day, time, class respectively
        # Classes labeled 'TBA' or 'Online-Only' are ignored
        if len(fields[2]) > 8 or fields[2] == 'TBA':
            pass
        else:
            day = fields[0]
            time_formatted = formatTime(fields[1])
            start_time = time_formatted[0]
            end_time = time_formatted[1]
            classroom = fields[2]
            classroom_row = (ID, classroom, start_time, end_time)
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
            weekdays = re.findall('[A-Z][^A-Z]*', day)
            for weekday in weekdays:
                cur.execute(insert_weekday_table, (ID, weekday))
            ID = ID + 1
        i += 11

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

    weekday_ref = ['Su', 'M', 'Tu', 'W', 'Th', 'F', 'Sa']

    weekday = weekday_ref[int(get_weekday(conn))]

    if conn is not None:
        # create table
        create_table(conn, create_classroom_table, 'classroom');
        create_table(conn, create_weekday_table, 'weekday');

        insert_classroom_data(conn);
        conn.commit()

        conn.close()
    else:
        print("Error! cannot create the database connection.")

main()
