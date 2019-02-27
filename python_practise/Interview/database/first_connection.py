# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# python script to connect to local oracle database
# and execute select query
#
# @reference: http://stackoverflow.com/questions/245465/cx-oracle-connecting-to-oracle-db-remotely
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cx_Oracle as db


def main():
    cx = ''
    cx_str = 'system/oracle@localhost:1521/xe'
    try:
        # Establish connection
        cx = db.connect(cx_str)
        print 'Connection established'

        # Create cursor
        cursor = cx.cursor()

        # Execute query
        query_str = 'select * from emp'
        cursor.execute(query_str)

        # Print result to the console
        print '-' * 80
        for result in cursor.fetchall():
            print result
        print '-' * 80

    finally:
        # Close connection
        if cx:
            cx.close()
            print("Connection closed!")

if __name__ == '__main__':
    main()

"""
C:\Python27\python.exe C:/Users/swadhi/Documents/bitbucket/pyselenium/PySelenium/python_practise/Interview/database/first_connection.py
Connection established
--------------------------------------------------------------------------------
('2001', 'Varun Sarkar', datetime.datetime(2009, 3, 1, 10, 0, 44), None)
('2002', 'Akshay Patel', datetime.datetime(2009, 3, 1, 10, 0, 44), '2001')
('2003', 'Naresh Chowdhary', datetime.datetime(2009, 3, 1, 10, 0, 44), '2001')
('2004', 'Anurag Sharma', datetime.datetime(2009, 3, 1, 10, 0, 44), '2001')
('2005', 'Das Gupta', datetime.datetime(2009, 3, 1, 10, 0, 44), '2003')
('2006', 'Ram Singh', datetime.datetime(2009, 3, 1, 10, 0, 44), '2003')
--------------------------------------------------------------------------------
Connection closed!

Process finished with exit code 0

"""