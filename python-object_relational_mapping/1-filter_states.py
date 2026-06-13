#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database
and lists all states starting with an uppercase 'N' from the table
'states', sorted in ascending order by states.id.
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

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                "ORDER BY states.id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
