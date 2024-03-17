#!/usr/bin/python3
import MySQLdb
import sys


def list_states(username, password, db_name):
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=db_name)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: {} < username > < password > < database > ".format(
                    sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(username, password, db_name)
