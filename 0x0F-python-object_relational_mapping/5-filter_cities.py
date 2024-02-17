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
    select {} from {} inner join {} on {} = {} where states.name = %s
    '''
    placeValue = (
        'cities.name', 'cities',
        'states', 'cities.state_id',
        'states.id'
    )

    cursor.execute(statement.format(*placeValue), (sys.argv[4], ))
    result = cursor.fetchall()

    for value in result:
        print(value[0], end='')

        if value != result[-1]:
            print(end=', ')
    print()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
