import PySimpleGUI as sg
import mysql.connector as sql_conn
from decimal import Decimal
import sys

sys.dont_write_bytecode = True

def check_null(num):
    if (num == ''):
        return None
    return Decimal(num)


def crear_teatro(values, usr, passw):
    nombre = values['snomt1e']
    telefono = values['stele']
    website = values['swebe']
    boleteria = values['stelbe']
    email = values['seme']
    capacidad = values['scape']
    print([nombre, Decimal(telefono), website, Decimal(boleteria), email, Decimal(capacidad)])

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_teatro', [nombre, Decimal(telefono), website, Decimal(boleteria), email, Decimal(capacidad)])
        sg.popup('Registrado con éxito')
    except (sql_conn.Error) as e:
        if (e.errno == 1370):
            sg.popup('Usted no tiene permiso para ejecutar esta funcionalidad')
        print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()


def crear_bloque(values, usr, passw):
    nombre = values['snombe']
    teatro = values['stbe']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_bloque', [nombre, teatro])

        sg.popup('Creado con éxito')
    except (sql_conn.Error) as e:
        if (e.errno == 1370):
            sg.popup('Usted no tiene permiso para ejecutar esta funcionalidad')
        print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()


def crear_fila(values, usr, passw):
    teatro = values['stfe']
    bloque = values['sbfe']
    cantidad = values['scane']
    letra = values['sle']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_fila', [teatro, bloque, Decimal(cantidad), letra])

        sg.popup('Creada con éxito')
    except (sql_conn.Error) as e:
        if (e.errno == 1370):
            sg.popup('Usted no tiene permiso para ejecutar esta funcionalidad')
        print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()


def registrar_admin_teatro(values, usr, passw):
    cedula = values['scede']
    nombre = values['snome']
    teatro = values['ste']
    fecha_nac = values['sfece']
    sexo = values['ssxe'].lower()
    direccion = values['sdire']
    tel_casa = check_null(values['stce'])
    celular = check_null(values['scele'])
    otro_tel = check_null(values['sote'])
    email = values['sem2e']
    user = values['suse']
    password = values['spasse']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_trn_registrar_admin_teatro', [Decimal(cedula), nombre, teatro, fecha_nac, sexo, direccion, tel_casa, celular, otro_tel, email, user, password])

        sg.popup('Registrado con éxito')
    except (sql_conn.Error) as e:
        num = e.errno
        if (num == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd")
        elif num == 1370:
            sg.popup('Usted no tiene permiso para ejecutar esta funcionalidad')
        elif num == 1644:
            sg.popup('La cédula o el usuario ya existe en el sistema')
        else:
            print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()
