#!/usr/bin/python3
"""
all rows from states by user input prevent sql injection
"""

import sys
import MySQLdb

if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) == 4:
        db = MySQLdb.connect(host='localhost', user=arguments[0],
                             passwd=arguments[1], db=arguments[2])
        cur = db.cursor()
        cur.execute("""SELECT * FROM states where states.name\
                    LIKE BINARY %(username)s\
                    order by states.id ASC""", {
                    'username': arguments[3]
                    })
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
