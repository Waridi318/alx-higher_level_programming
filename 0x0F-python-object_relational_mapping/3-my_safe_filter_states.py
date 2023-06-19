#!/usr/bin/python3
"""
This module hat takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    search_arg = sys.argv[4]
    cur.execute(query, (search_arg,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
