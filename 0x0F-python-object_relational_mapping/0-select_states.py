#!/usr/bin/python3
import sys
import MySQLdb

"""
select all rows from states
"""

if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) == 3:
        db = MySQLdb.connect(host='localhost', user=arguments[0],
                             passwd=arguments[1], db=arguments[2])
        cur = db.cursor()
        cur.execute("SELECT * FROM states order by states.id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
