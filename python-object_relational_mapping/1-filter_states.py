#!/usr/bin/python3
"""Lists all states from database BUT they have to start with N"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id")
    """added in the specified letter start type"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()