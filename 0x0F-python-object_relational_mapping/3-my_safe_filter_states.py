#!/usr/bin/python3
'''mysql connection with MySQLdb'''
import sys
import MySQLdb


def main():
    '''function that selects items from a database'''
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = conn.cursor()
    statement = '''
    select * from states where name = %s order by id asc
    '''

    cursor.execute(statement, (sys.argv[4], ))

    for value in cursor:
        print(value)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
