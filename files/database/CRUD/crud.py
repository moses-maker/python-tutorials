import sqlite3
from datetime import datetime
from prettytable import PrettyTable

"""
open_database() function will return conn object that
will be used for CRUD operations.
"""
def open_database():
    database = "register.db"
    print("Connecting to SQLITE...")
    connection = sqlite3.connect(database)
    print('Connected')
    return connection

def create_table(connection):
    # Firstly, we obtain cursor by calling conn.cursor().
    cursor = connection.cursor()
    # We define creating table query in sql variable
    sql = ''' 
            create table if not exists student(
            reg_number integer primary key,
            name char(30) not null,
            phone_number integer,
            marks integer,
            created text)
          '''
    # we execute a query using cursor.execute().
    cursor.execute(sql)
    # After executed, you should call conn.commit() to commit all 
    # data changes.
    connection.commit()
    print("Created a table ")


def create_data(connection):
    cursor = connection.cursor()
    #current_date= datetime.now().strftime("%Y-%m-%d")
    reg_number = int(input("Enter registration number?"))
    name = input("Enter your name?")
    phone= int(input("Enter your phone number?"))
    marks = int(input("Enter your marks?s"))
    date_created = input("Enter the date?")
    print("Inserting data...")
    cursor.execute("INSERT INTO student(reg_number, name, phone_number, marks, created) VALUES(?, ?, ?, ?, ?)",
                   (reg_number, name, phone, marks, date_created ))
    connection.commit()
    cursor.close()
    print("Done")


# open data
connection = open_database()

# creating table 
#create_table(connection)

# creating data
create_data(connection)

# close data
connection.close()


