#!/usr/bin/python3
""" lists all states from the database hbtn0e0usa """
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    mydb.close()
