#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database
and safely displays all values in the states table where the name
matches the argument provided, protected against SQL injections.
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

    # Using %s placeholder and passing sys.argv[4] as a parameter tuple
    # to guarantee safety against malicious SQL injections
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cur.execute(query, (sys.argv[4],))

    # Fetch and display all matching rows
    for row in cur.fetchall():
        print(row)

    # Close the cursor and the database connection properly
    cur.close()
    db.close()
