import sqlite3
from datetime import datetime
# Connection to SQlite
connection = sqlite3.connect("example.db")

# create a cursor object
cursor_object = connection.cursor()

# create the table
cursor_object.execute('''
        CREATE TABLE IF NOT EXISTS students(
                            regnumber INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            phonenumber TEXT NOT NULL,
                            marks INTEGER NOT NULL,
                            created TEXT NOT NULL )
                            ''')

#function to insert data to table
def insert_data(regnumber, name, phonenumber, marks):
    currentdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor_object.execute('''
                          INSERT INTO students(regnumber, name, phonenumber,marks, created)
                          VALUES(?,?,?,?,?)
                          ''', (regnumber, name, phonenumber, marks, currentdate))
    
students = [
    (1, "Alice Johnson", 987, 97),
    (2, "Peter Maina", 487, 95),
    (3, "James Gishuru", 988, 93),
    (4, "James Rice", 900, 80),
    (5, "John Nyaga",467, 47)
]

for student in students:
    insert_data(*student)

connection.commit()
