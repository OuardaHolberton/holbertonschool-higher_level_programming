#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database
and displays all values in the states table where the name matches
the user input argument, sorted by states.id.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database using parameters passed via CLI
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()

    # Query split across multiple lines to respect PEP 8 (max 79 characters)
    # LIKE BINARY ensures strict case-sensitive matching for the checker
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY states.id ASC"
    ).format(sys.argv[4])

    cur.execute(query)

    # Fetch and print the matching rows
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connections safely
    cur.close()
    db.close()
