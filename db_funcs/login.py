import mysql.connector as sql_conn
import sys

sys.dont_write_bytecode = True

def validate_login(user, passw):
    try:
        db = sql_conn.connect(user = user, password = passw, host = 'localhost', database = 'progra2')
        db.close()
        return True
    except(sql_conn.Error) as e:
        if e.errno == 1045:
            return False