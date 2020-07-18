import mysql.connector as sql_conn

def validate_login(user, passw):
    try:
        db = sql_conn.connect(user = user, password = passw, host = 'localhost', database = 'progra2')
        db.close()
        return True
    except(sql_conn.Error) as e:
        if e.errno == 1045:
            return False