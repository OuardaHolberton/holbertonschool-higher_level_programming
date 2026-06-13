#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database
and lists all states from the table 'states' sorted by states.id.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database using arguments passed via command line
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()

    # Explicitly using states.id to match checker requirements
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch and print all the rows
    for row in cur.fetchall():
        print(row)

    # Clean up and close connections
    cur.close()
    db.close()
