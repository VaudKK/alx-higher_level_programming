#!/usr/bin/python3
"""
all rows from states by user input
"""

import sys
import MySQLdb

if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) == 4:
        db = MySQLdb.connect(host='localhost', user=arguments[0],
                             passwd=arguments[1], db=arguments[2])
        cur = db.cursor()
        query = "SELECT * FROM states where states.name LIKE BINARY '{}'\
                 order by states.id ASC".format(arguments[3])
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
