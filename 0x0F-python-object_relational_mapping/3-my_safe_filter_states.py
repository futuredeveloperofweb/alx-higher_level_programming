#!/usr/bin/python3
'''write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from MySQL
injections'''
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    m = sys.argv[4]
    cur.execute('SELECT * FROM states WHERE BINARY name LIKE %s', (m,))
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    db.close()
