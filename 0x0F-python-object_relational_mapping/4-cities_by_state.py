#!/usr/bin/python3

"""
This module lists all cities from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()
