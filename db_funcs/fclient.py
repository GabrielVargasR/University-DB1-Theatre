import PySimpleGUI as sg
import mysql.connector as sql_conn
from decimal import Decimal
from math import floor
from random import randint
from datetime import datetime
import sys

sys.dont_write_bytecode = True


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


def print_factura(titulo, fecha, bloque, fila, asientos, nombre, monto, codigo, fecha_compra):
    mensaje = 'Factura\n\n'
    mensaje += 'Título presentación: ' + titulo + '\n'
    mensaje += 'Fecha: ' + fecha + '\n'
    mensaje += 'Bloque: ' + bloque + '\n'
    mensaje += 'Asientos: '

    for a in asientos:
        mensaje += str(a) + fila + '  '

    mensaje += 'Nombre cliente: ' + nombre + '\n'
    mensaje += 'Monto: ' + monto + '\n'
    mensaje += 'Código de compra: ' + codigo + '\n'
    mensaje += 'Fecha compra: ' + fecha_compra + '\n'

    sg.popup(mensaje)


def get_precio_bloque(titulo, fecha, bloque):
    try:
        db = sql_conn.connect(user = 'root', password = 'vmDTNoK1&b', host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        results = cursor.callproc('sp_read_precio_bloque', [titulo, fecha, bloque, 0])
        return results[3]

    except(sql_conn.Error) as e:
        print('Hubo un problema con la conexión')
    finally:
        cursor.close()
        db.close()


def validar_transaccion(nombre, num_tarjeta, exp, cvv, monto):
    if ((cvv+floor(monto)) % 2 != 0):
        fecha = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        return (True, randint(100000, 999999), fecha)
    return (False)


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
    asientos = [int(i) for i in values['pne'].replace(" ", "").split(",")]

    nombre = values['pnome']
    tarjeta = values['ptare']
    expiracion = values['pexte']
    cvv = values['pcte']
    monto = get_precio_bloque(titulo, fecha, bloque)
    total = monto * len(asientos)
    valid = validar_transaccion(nombre, tarjeta, expiracion, cvv, monto)

    if (valid[0]==False):
        sg.popup('Su tarjeta fue rechazada')
        return

    try:
        db = sql_conn.connect(user = 'cliente_teatro', password = 'cliente123', host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_read_asientos_disponibles', [titulo, fecha, bloque])

        print_factura(titulo, fecha, bloque, fila, asientos, nombre, total, valid[1], valid[2])

    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd hh:mm:ss")
        else:
            print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()


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
    
