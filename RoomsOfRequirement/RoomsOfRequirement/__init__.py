import sqlite3
from sqlite3 import Error


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

    print(weekday)
    if conn is not None:
        # create table
        create_table(conn, create_classroom_table, 'classroom');
        create_table(conn, create_weekday_table, 'weekday');
        conn.commit()

        conn.close()
    else:
        print("Error! cannot create the database connection.")

main()
