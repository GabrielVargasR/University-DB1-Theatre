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
        results = cursor.callproc('sp_read_teatro_usuario', [usr,0])
        result = results[1]

        cursor.close()
        db.close()
        return result

    except (sql_conn.Error) as e:
        print(e)


def print_cartelera(cartelera):
    headings = ['Título', 'Teatro', 'Fecha', 'Hora', 'Precios']
    info = []

    for p in cartelera:
        info.append([p[0], p[1], p[2].strftime('%d/%m/%Y'), p[2].strftime('%H:%M:%S'), p[3]])

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


def print_factura(titulo, pfecha, bloque, fila, asientos, nombre, monto, codigo, fecha_compra):

    fecha = datetime.strptime(pfecha, '%Y-%m-%d %H:%M:%S')

    mensaje = 'Factura\n\n'
    mensaje += 'Título presentación: ' + titulo + '\n'
    mensaje += 'Fecha: ' + fecha.strftime('%d/%m/%Y') + '\n'
    mensaje += 'Hora: ' + fecha.strftime('%H:%M:%S') + '\n'
    mensaje += 'Bloque: ' + bloque + '\n'
    mensaje += 'Asientos: '

    for a in asientos:
        mensaje += str(a) + fila + '  '

    mensaje += '\nNombre cliente: ' + nombre + '\n'
    mensaje += 'Monto: ' + str(monto) + '\n'
    mensaje += 'Código de compra: ' + str(codigo) + '\n'
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
    return (False,0,0)


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
    cvv = int(values['pcte'])
    monto = get_precio_bloque(titulo, fecha, bloque)
    total = monto * len(asientos)
    valid = validar_transaccion(nombre, tarjeta, expiracion, cvv, monto)

    if (valid[0]==False):
        sg.popup('Su tarjeta fue rechazada')
        return
    
    if(len(asientos) > 8):
        sg.popup('Seleccionó más asientos de los permitidos. Intente otra vez')
        return

    try:
        db = sql_conn.connect(user = 'cliente_teatro', password = 'cliente123', host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        params = [a for a in asientos]

        for i in range(8-len(asientos)):
            params += [None]

        params += [titulo, bloque, fila, fecha, nombre, total, valid[1], valid[2]]    
        cursor.callproc('sp_trn_comprar_tiquete', params)

        print_factura(titulo, fecha, bloque, fila, asientos, nombre, total, valid[1], valid[2])

    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd hh:mm:ss")
        elif (e.errno == 1644):
            sg.popup("Alguno de los asientos que eligió no está disponible")
        else:
            print(e)
    except TypeError as e2:
        print(e2)
        sg.popup('Hay un problema con el formato de sus datos')
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
    asientos = [int(i) for i in values['gne'].replace(" ", "").split(",")]

    nombre = values['gnome']
    tarjeta = values['gtare']
    expiracion = values['gexte']
    cvv = values['gcte']
    monto = get_precio_bloque(titulo, fecha, bloque)
    total = monto * len(asientos)

    if(len(asientos) > 8):
        sg.popup('Seleccionó más asientos de los permitidos. Intente otra vez')
        return

    if pago == 'Tarjeta': 
        tarjeta = tarjeta
        cvv = int(cvv)
        valid = validar_transaccion(nombre, tarjeta, expiracion, cvv, monto)
        if (valid[0]==False):
            sg.popup('Su tarjeta fue rechazada')
            return
    elif pago == 'Efectivo':
        valid = (True, 0, datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        tarjeta = None
        cvv = None


    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        params = [a for a in asientos]

        for i in range(8-len(asientos)):
            params += [None]

        params += [titulo, bloque, fila, fecha, nombre, total, valid[1], valid[2]]    
        cursor.callproc('sp_trn_comprar_tiquete', params)

        print_factura(titulo, fecha, bloque, fila, asientos, nombre, total, valid[1], valid[2])

    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd hh:mm:ss")
        elif (e.errno == 1644):
            sg.popup("Alguno de los asientos que eligió no está disponible")
        else:
            print(e)
    except TypeError as e2:
        print(e2)
        sg.popup('Hay un problema con el formato de los datos')
    finally:
        db.commit()
        cursor.close()
        db.close()

