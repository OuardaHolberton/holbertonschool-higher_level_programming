#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database
and lists all cities along with their corresponding state names
from the database, sorted in ascending order by cities.id.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
