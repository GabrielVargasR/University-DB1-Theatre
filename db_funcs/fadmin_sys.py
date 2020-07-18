import PySimpleGUI as sg
import mysql.connector as sql_conn


def crear_teatro(values, usr, passw):
    nombre = values['snomt1e']
    telefono = values['stele']
    website = values['swebe']
    boleteria = values['stelbe']
    email = values['seme']
    capacidad = values['scape']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_teatro', [nombre, telefono, website, boleteria, email, capacidad])

        cursor.close()
        db.close()
    except (sql_conn.Error) as e:
        print(e)


def crear_bloque(values, usr, passw):
    nombre = values['snombe']
    teatro = values['stbe']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_bloque', [nombre, teatro])

        cursor.close()
        db.close()
    except (sql_conn.Error) as e:
        print(e)


def crear_fila(values, usr, passw):
    teatro = values['stfe']
    bloque = values['sbfe']
    cantidad = values['scane']
    letra = values['sle']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_fila', [teatro, bloque, cantidad, letra])

        cursor.close()
        db.close()
    except (sql_conn.Error) as e:
        print(e)


def registrar_admin_teatro(values, usr, passw):
    cedula = values['scede']
    nombre = values['snome']
    teatro = values['ste']
    fecha_nac = values['sfece']
    sexo = values['ssxe']
    direccion = values['sdire']
    tel_casa = values['stce']
    celular = values['scele']
    otro_tel = values['sote']
    email = values['sem2e']
    user = values['suse']
    password = values['spasse']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_trn_registrar_admin_teatro', [cedula, nombre, teatro, fecha_nac, sexo, direccion, tel_casa, celular, otro_tel, email, user, password])

        cursor.close()
        db.close()
    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd")
        else:
            print(e)