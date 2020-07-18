import PySimpleGUI as sg
import mysql.connector as sql_conn

def print_cartelera(cartelera):
    str_cartelera = ''

    for i in cartelera:
        str_cartelera += i + '\n'


def get_teatro(usr):
    db = sql_conn.connect(user = 'root', password = 'vmDTNoK1&b', host = 'localhost', database = 'progra2')
    cursor = db.cursor()
    try:
        results = cursor.callproc('sp_read_teatro_usuario', [usr,1,0])
        result = results[2]

        cursor.close()
        db.close()
        return result

    except (sql_conn.Error) as e:
        print(e)
        

def consultar_cartelera_cliente(values, usr, passw):
    db = sql_conn.connect(user = 'cliente_teatro', password = 'cliente123', host = 'localhost', database = 'progra2')
    cursor = db.cursor()
    
    fi = values['pfie']
    ff = values['pffe']
    try:
        cursor.callproc('sp_read_cartelera', [fi,ff])
        result = next(cursor.stored_results())
        cartelera = ['No hay presentaciones en esas fechas']

        x=0
        for i in result:
            cartelera[x] = i
            x+=x

        cursor.close()
        db.close()

        sg.popup(cartelera)
    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha")


def consultar_asientos_cliente(values, usr, passw):
    db = sql_conn.connect(user = 'cliente_teatro', password = 'cliente123', host = 'localhost', database = 'progra2')
    cursor = db.cursor()

    titulo = values['pttl1e']
    fecha = values['pfp1e']
    bloque = values['pbl1e']

    try:
        cursor.callproc('sp_read_asientos_disponibles', [titulo, fecha, bloque])
        result = next(cursor.stored_results())
        asientos = ['No hay asientos disponibles en ese bloque']

        x=0
        for i in result:
            asientos[x] = i
            x+=x

        cursor.close()
        db.close()

        sg.popup(asientos)
    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd hh:mm:ss")


def comprar_entradas_cliente(values, usr, passw):
    titulo = values['pttl2e']
    fecha = values['pfp2e']
    bloque = values['pbl2e']
    fila = values['pfe']
    #nums = [int(i) for i in values['pne'].replace(" ", "").split(",")]
    sg.popup('comprar_entradas_cliente')


def consultar_cartelera_agente(values, usr, passw):
    db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
    cursor = db.cursor()
    
    fi = values['gfie']
    ff = values['gffe']
    try:
        cursor.callproc('sp_read_cartelera', [fi,ff])
        result = next(cursor.stored_results())
        cartelera = ['No hay presentaciones en esas fechas']

        x=0
        for i in result:
            cartelera[x] = i
            x+=x

        cursor.close()
        db.close()

        sg.popup(cartelera)
    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha")


def consultar_asientos_agente(values, usr, passw):
    db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
    cursor = db.cursor()

    titulo = values['gttl1e']
    fecha = values['gfp1e']
    bloque = values['gbl1e']

    try:
        cursor.callproc('sp_read_asientos_disponibles', [titulo, fecha, bloque])
        result = next(cursor.stored_results())
        asientos = ['No hay asientos disponibles en ese bloque']

        x=0
        for i in result:
            asientos[x] = i
            x+=x

        cursor.close()
        db.close()

        sg.popup(asientos)
    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd hh:mm:ss")


def vender_entradas_agente(values, usr, passw):
    titulo = values['gttl2e']
    fecha = values['gfp2e']
    bloque = values['gbl2e']
    fila = values['gfe']
    pago = values['gpge']
    nums = [int(i) for i in values['gne'].replace(" ", "").split(",")]
    sg.popup('vender_entradas_agente')
    
