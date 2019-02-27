# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# python script to connect to local oracle database
# and execute select query with and statement
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cx_Oracle as oracle

cx_string = 'system/oracle@localhost:1521/xe'
query_str = 'select * from employee where emp_id > 2002 and emp_id < 2007'


def main():
    # Create connnection instance
    cx = oracle.connect(cx_string)
    print("Connection established!")

    try:
        # Create cursor
        cursor = cx.cursor()

        # Execute query
        cursor.execute(query_str)

        # Process output
        print '-' * 100
        for result in cursor.fetchall():
            print result
        print '-' * 100
    finally:
        if cx:
            cx.close()
            print("Oracle connection closed!")

if __name__ == '__main__':
    main()

"""
C:\Python27\python.exe C:/Users/swadhi/Documents/bitbucket/pyselenium/PySelenium/python_practise/Interview/database/second_connection.py
Connection established!
----------------------------------------------------------------------------------------------------
(2003, 1, 'Tim', 'Knitter', 'SrEngineer', datetime.datetime(2011, 3, 30, 10, 0, 44), 6000.0)
(2004, 1, 'Sidney', 'Sheldon', 'Engineer', datetime.datetime(2013, 10, 10, 10, 0, 44), 3500.0)
(2005, 1, 'Michael', 'Slater', 'JrEngineer', datetime.datetime(2014, 11, 13, 10, 0, 44), 3000.0)
(2006, 2, 'David', 'Seller', 'SrEngineer', datetime.datetime(2010, 4, 9, 10, 0, 44), 5400.0)
----------------------------------------------------------------------------------------------------
Oracle connection closed!

Process finished with exit code 0
"""