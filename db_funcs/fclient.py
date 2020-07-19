import PySimpleGUI as sg
import mysql.connector as sql_conn
from decimal import Decimal
import sys

sys.dont_write_bytecode = True

def print_cartelera(cartelera):
    headings = ['Título', 'Teatro', 'Fecha', 'Hora', 'Precios']
    info = []

    for p in cartelera:
        info.append([p[0], p[1], p[2].strftime('%m/%d/%Y'), p[2].strftime('%H:%M:%S'), p[3]])

    if (info == []):
        info = [['-', '-', '-', '-', '-']]
    
    table = [[sg.Table(info, headings=headings, auto_size_columns=True, max_col_width=80, hide_vertical_scroll=True, select_mode='extended', justification='center')]]
    pop_window = sg.Window('Cartelera', table)

    while True:
        event, values = pop_window.read()
        print(event)
        if event == None:
            break
    pop_window.close()


def print_asientos(asientos):
    str_asientos = ''
    current = ''

    for f in asientos:
        if current != f[0]:
            current = f[0]
            str_asientos += '\n' + current + ': ' + str(f[1])
        else:
            str_asientos += ', ' + str(f[1])


    if str_asientos == '':
        sg.popup('No hay ningún asiento disponible en este bloque')
        return

    sg.popup(str_asientos)


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
        print_cartelera(result)


    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha")
    finally:
        cursor.close()
        db.close()


def consultar_asientos_cliente(values, usr, passw):
    db = sql_conn.connect(user = 'cliente_teatro', password = 'cliente123', host = 'localhost', database = 'progra2')
    cursor = db.cursor()

    titulo = values['pttl1e']
    fecha = values['pfp1e']
    bloque = values['pbl1e']

    try:
        cursor.callproc('sp_read_asientos_disponibles', [titulo, fecha, bloque])
        result = next(cursor.stored_results())
        print_asientos(result)
        
    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd hh:mm:ss")
    finally:
        cursor.close()
        db.close()


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
        print_cartelera(result)


    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha")
    finally:
        cursor.close()
        db.close()


def consultar_asientos_agente(values, usr, passw):
    db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
    cursor = db.cursor()

    titulo = values['gttl1e']
    fecha = values['gfp1e']
    bloque = values['gbl1e']

    try:
        cursor.callproc('sp_read_asientos_disponibles', [titulo, fecha, bloque])
        result = next(cursor.stored_results())
        print_asientos(result)
        
    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd hh:mm:ss")
    finally:
        cursor.close()
        db.close()


def vender_entradas_agente(values, usr, passw):
    titulo = values['gttl2e']
    fecha = values['gfp2e']
    bloque = values['gbl2e']
    fila = values['gfe']
    pago = values['gpge']
    nums = [int(i) for i in values['gne'].replace(" ", "").split(",")]
    sg.popup('vender_entradas_agente')
    
