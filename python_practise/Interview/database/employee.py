# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# python program to List all employees with their supervisor names
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cx_Oracle as db

query_str = """select a.emp_id as "EMP_ID", a.EMP_NAME as "NAME", \
b.EMP_ID as "MANAGER_ID", b.EMP_NAME as "MANAGER_NAME" \
from emp a, emp b \
where a.emp_supv = b.emp_id"""

connect_str = 'system/oracle@localhost:1521/xe'


def main():
    # Create connection
    cx = db.connect(connect_str)

    try:
        # Create cursor
        cursor = cx.cursor()

        # Execute query
        cursor.execute(query_str)
        print("Executed query: {}".format(query_str))

        # Print headers
        columns = [i[0] for i in cursor.description]
        for column_name in columns:
            print column_name,
        print

        # Parse result and display
        for result in cursor.fetchall():
            print(result)

    finally:
        if cx:
            cx.close()
            print("Connection closed")

if __name__ == '__main__':
    main()
