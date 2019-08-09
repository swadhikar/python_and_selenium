from contextlib import contextmanager
from datetime import datetime as dt
import sqlite3  # A light weight database


insert_query = 'insert into department values (4, "Marketing", 432532);'



@contextmanager
def open_sqlite3_db(dbname='test.db'):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        yield conn.cursor()
    except Exception as e:
        print("Error occcured during DB operations! Caused by:\n",e)
    finally:
        # conn.commit() # TODO: Uncomment this line
        conn.close()    # Resource cleanup
        print("Db connection has been closed!")


if __name__ == '__main__':
    with open_sqlite3_db() as db_cursor:
        db_cursor.execute(insert_query)
        print('Data inserted successfully!')
