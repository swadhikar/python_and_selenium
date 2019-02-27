import cx_Oracle as oracle


class OracleDriver(object):
    def __init__(self, user='system', password='oracle', host='localhost', port='1521', sid='xe'):
        self.connection_string = self.get_connection_string(user, password, host, port, sid)
        self.connection = self.__get_connection()

    @staticmethod
    def get_connection_string(user, password, host, port, sid):
        user = str(user)
        password = str(password)
        host = str(host)
        port = str(port)
        sid = str(sid)

        conn_str = "{user}/{password}@{host}:{port}/{sid}".format(user=user,
                                                                  password=password,
                                                                  host=host,
                                                                  port=port,
                                                                  sid=sid)
        print("DEBUG: Connection string: " + conn_str)
        return conn_str

    def __get_connection(self):
        # Create a connection to the database and return connection object
        return oracle.connect(self.connection_string)

    def __query_type(self, query_str):
        query_type = query_str.split(' ')[0]
        print("DEBUG: Query type '{}'".format(query_type))
        return query_type

    def execute(self, query_str):
        """Executes a given string and does not return result"""
        connection = self.connection
        cursor = connection.cursor()

        try:
            print("Executing query: " + str(query_str))
            cursor.execute(query_str)
            connection.commit()
        finally:
            connection.close()

        print("Query Execution successful!")

    def execute_get(self, query_str):
        """Executes a given string and does not return result"""
        connection = self.connection
        cursor = connection.cursor()

        try:
            print("INFO:  Executing query: " + str(query_str))
            cursor.execute(query_str)
            result_set = cursor.fetchall()
        finally:
            connection.close()

        return result_set


if __name__ == '__main__':
    def select():
        query_str = """select a.emp_id as "EMP_ID", a.EMP_NAME as "NAME", \
    b.EMP_ID as "MANAGER_ID", b.EMP_NAME as "MANAGER_NAME" \
    from emp a, emp b \
    where a.emp_supv = b.emp_id"""

        driver = OracleDriver()
        rs = driver.execute_get(query_str)

        print "\n{} {}, {}, {}".format("EMP_ID", "EMP_NAME", "MGR_ID", "MGR_NAME")

        for r in rs:
            (emp_id, emp_name, mgr_id, mgr_name) = r
            print "{}, {}, {}, {}".format(emp_id, emp_name, mgr_id, mgr_name)


    def insert():
        query_str = "insert into " \
                    "emp values(2010, 'Zaheer Khan', " \
                    "TO_DATE('2014/04/09', 'yyyy/mm/dd'), 2001)"

        driver = OracleDriver()
        driver.execute(query_str)


    # insert()
    # select()
    pass
