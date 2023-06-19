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
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name LIKE BINARY '{}' "
        "ORDER BY cities.id ASC".format(sys.argv[4])
    )

    cities = cur.fetchall()
    if cities:
        city_list = [city[0] for city in cities]
        city_string = ", ".join(city_list)
        print(city_string)

    else:
        print()

    cur.close()
    db.close()
