import PySimpleGUI as sg
import mysql.connector as sql_conn

db = sql_conn.connect(user = 'root', password = 'vmDTNoK1&b', host = 'localhost', database = 'progra1')
cursor = db.cursor()

'''
# Informal way of calling a param
cursor.execute('CALL ReadPersonas') 
result = cursor.fetchall()
for i in result:
    print(i) # i es una lista, entonces se puede indexar
'''


# Calling proc without parameters
cursor.callproc('ReadPersonas')
result = next(cursor.stored_results()) # cursor.stored_result() returns a Generator object that behaves like an iterator
# for row in result:
#     print(row)
names = [i[2] for i in result]
sg.popup(names)



# Calling a proc with parameters
cursor.callproc('ReadPartesAuto', ['Camry', 2015])
result2 = next(cursor.stored_results())
for i in result2:
    print(i)



# End of query
cursor.close()
db.close()


# ver https://www.mysqltutorial.org/calling-mysql-stored-procedures-python/
# ahí está lo de out parameters: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-callproc.html