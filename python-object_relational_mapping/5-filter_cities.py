#!/usr/bin/python3
"""
This module provides a script that takes the name of a state as an
argument and lists all cities of that state from the database,
safely protected against SQL injections and formatted as a string.
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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query, (sys.argv[4],))
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))
    cur.close()
    db.close()
