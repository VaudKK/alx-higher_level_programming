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
        cur.execute("""SELECT cities.name FROM cities where cities.state_id\
                    = (SELECT states.id FROM states WHERE\
                    states.name LIKE BINARY %(statename)s)\
                    """, {
                    'statename': arguments[3]
                    })
        rows = cur.fetchall()
        if rows is not None:
            print(", ".join(row[0] for row in rows))

        cur.close()
        db.close()
