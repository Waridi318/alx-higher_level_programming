#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


def list_states(username, password, database):
    """
    Lists all states in the databse
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database
    )

    cursor = db.cursor()
    try:
        cursor.execute(
            "SELECT * FROM states "
            "WHERE name LIKE BINARY 'N%' "
            "ORDER BY id ASC"
        )
        rows = cursor.fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        print("Error")

    for row in rows:
        print(row)


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
