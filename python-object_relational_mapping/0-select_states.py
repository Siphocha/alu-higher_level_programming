#!/usr/bin/python3
"""Script listing all states from hbtn_0e_0_usa
This script connects to MYSQL server on localhost on a port.
retrieves all rows from states sorted in ASCENDING order"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]
    """We use the sys because database stored locally"""
    db = MySQLdb.connect(host="localhost", port=3306,  user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    """fetching from the database using SELECT and fetchall again."""
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
