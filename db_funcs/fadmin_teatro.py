import PySimpleGUI as sg
import mysql.connector as sql_conn
from decimal import Decimal
import sys

sys.dont_write_bytecode = True


def get_teatro(usr):
    db = sql_conn.connect(user = 'root', password = 'vmDTNoK1&b', host = 'localhost', database = 'progra2')
    cursor = db.cursor()
    try:
        results = cursor.callproc('sp_read_teatro_usuario', [usr,0,0])
        result = results[2]

        cursor.close()
        db.close()
        return result

    except (sql_conn.Error) as e:
        print(e)


def check_null(num):
    if (num == ''):
        return None
    return Decimal(num)


def definir_produccion(values, usr, passw):
    titulo = values['ttl1e']
    descripcion = values['tdese']
    tipo = values['ttipe']
    teatro = get_teatro(usr)

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_nueva_produccion', [titulo, descripcion, tipo, teatro])

        sg.popup('Producción registrada exitosamente')
    except (sql_conn.Error) as e:
        num = e.errno
        if num == 1370:
            sg.popup('Usted no tiene permiso para esta funcionalidad')
        print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()


def definir_presentacion(values, usr, passw):
    teatro = get_teatro(usr)
    titulo = values['ttl2e']
    fecha = values['tfece']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_presentacion', [teatro, titulo, fecha])

        sg.popup('Presentación registrada con éxito')
    except (sql_conn.Error) as e:
        if (e.errno == 1292):
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd hh:mm:ss")
        else:
            print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()


def definir_precio(values, usr, passw):
    teatro = get_teatro(usr)
    titulo = values['ttl3e']
    bloque = values['tble']
    precio = values['tpre']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_create_precio_bloque', [teatro, titulo, bloque, precio])

        sg.popup('Precio definido exitosamente')
    except (sql_conn.Error) as e:
        num = e.errno
        if num == 1370:
            sg.popup('Usted no tiene permiso para esta funcionalidad')
        print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()


def camiar_estado_presentacion(values, usr, passw):
    teatro = get_teatro(usr)
    titulo = values['ttl4e']
    estado = values['tese'].lower()

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_update_estado_produccion', [teatro, titulo, estado])

        sg.popup('Estado cambiado con éxito')
    except (sql_conn.Error) as e:
        num = e.errno
        if num == 1370:
            sg.popup('Usted no tiene permiso para esta funcionalidad')
        print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()


def registrar_agente(values, usr, passw):
    teatro = get_teatro(usr)
    cedula = values['tcede']
    nombre = values['tnome']
    fecha_nac = values['tfecne']
    sexo = values['tsxe']
    direccion = values['tdire']
    tel_casa = check_null(values['ttce'])
    celular = check_null(values['tcele'])
    otro_tel = check_null(values['tote'])
    email = values['teme']
    user = values['tuse']
    password = values['tpasse']

    try:
        db = sql_conn.connect(user = usr, password = passw, host = 'localhost', database = 'progra2')
        cursor = db.cursor()

        cursor.callproc('sp_trn_registrar_agente', [teatro, Decimal(cedula), nombre, fecha_nac, sexo, direccion, tel_casa, celular, otro_tel, email, user, password])

        sg.popup('Agente registrado con éxito')
    except (sql_conn.Error) as e:
        num = e.errno
        if num == 1292:
            sg.popup("Formato incorrecto para fecha\naaaa-mm-dd")
        elif num == 1370:
            sg.popup('Usted no tiene permiso para esta funcionalidad')
        print(e)
    finally:
        db.commit()
        cursor.close()
        db.close()
