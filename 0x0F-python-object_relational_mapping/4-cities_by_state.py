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
    select {}, {}, {} from {} inner join {} on {} = {} order by {} asc
    '''
    placeValue = (
        'cities.id', 'cities.name',
        'states.name', 'cities',
        'states', 'cities.state_id',
        'states.id', 'cities.id'
    )

    cursor.execute(statement.format(*placeValue))

    for value in cursor:
        print(value)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
