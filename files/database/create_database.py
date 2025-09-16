# this is a module used to create database
import sqlite3

# this is the database file with extention .db
db = "registration.db"

# pass database file to connect() method
conn = sqlite3.connect(db)

print("connected ")
print(conn)
conn.close()

