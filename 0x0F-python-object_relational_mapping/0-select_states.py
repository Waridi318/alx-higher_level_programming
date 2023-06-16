#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    password="Selina@12",
    database="hbtn_0e_0_usa"
)

cursor = db.cursor()
try:
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
except Exception as e:
    print("Error")

for row in rows:
    print(row)
