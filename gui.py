import PySimpleGUI as sg
import db_funcs.fclient as dbc
import db_funcs.fadmin_teatro as dbt 
import db_funcs.fadmin_sys as dbs 
import db_funcs.login as val

#                                                                    #                                 |    Público     |  'p..'
# ------------------------------------------------------------------ #                                 | Agente teatro  |  'g..'
# --------------------------- Variables ---------------------------- #                                 | Admin. teatro  |  't..'
# ------------------------------------------------------------------ #                                 | Admin. sistema |  's..'

sg.theme('light grey 6')
screen = (1000,800)
my_font = ('Arial', 14)

current_frame = 'pf1'
logged = False
current_fn = 0

username = ''
password = ''

frames = {'Consultar cartelera::pm1':['pf1',0], 'Consultar asientos::pm2':['pf2',0], 'Comprar tiquetes::pm3':['pf3',0],
          'Consultar cartelera::gm1':['gf1',1], 'Consultar asientos::gm2':['gf2',1], 'Vender tiquetes::gm3':['gf3',1],
          'Definir nueva producción::tm1':['tf1',2], 'Definir calendario producción::tm2':['tf2',2], 'Definir precios producción::tm3':['tf3',2],
                    'Cambiar estado de producción::tm4':['tf4',2], 'Incluir agente autorizado::tm5':['tf5',2],
          'Agregar teatro::sm1':['sf1',3], 'Agregar administrador teatro::sm2':['sf2',3] }

buttons = {'pb1':dbc.consultar_cartelera_cliente, 'pb2':dbc.consultar_asientos_cliente, 'pb3':dbc.comprar_entradas_cliente,
           'gb1':dbc.consultar_cartelera_agente, 'gb2':dbc.consultar_asientos_agente, 'gb3':dbc.vender_entradas_agente,
           'tb1':dbt.definir_produccion, 'tb2':dbt.definir_presentacion, 'tb3':dbt.definir_precio, 'tb4':dbt.camiar_estado_presentacion, 'tb5':dbt.registrar_agente,
           'sb1a':dbs.crear_teatro, 'sb1b':dbs.crear_bloque, 'sb1c':dbs.crear_fila, 'sb2':dbs.registrar_admin_teatro}

def login_handler(current_frame):
    while True:
        event, values = main_window.read()
        if event == None:
            break
        elif event == 'blogin':
            global username
            global password
            username = values['usuario_login']
            password = values['password_login']
            if val.validate_login(username, password):
                main_window['usuario_login'].update('')
                main_window['password_login'].update('')
                main_window['login_frame'].update(visible=False)
                main_window[current_frame].update(visible=True)
                break
            else:
                sg.popup('El usuario o la contraseña son incorrectos. Por favor intente de nuevo')


# ------------------------------------------------------------------ #
# ---------------- Functions for layout definition ----------------- #
# ------------------------------------------------------------------ #
def input_info(lab, text_key, in_key, in_size=(45,1)):
    # falta meterle key al text
    return [sg.Text(lab, key=text_key), sg.Input(key=in_key, size=in_size)]

def col(pLayout, pKey):
    return sg.Column(pLayout, size=screen, key=pKey, visible=False)


# ------------------------------------------------------------------ #
# --------------------------- Layouts ------------------------------ #
# ------------------------------------------------------------------ #
menu_def = [['Clientes',['Consultar cartelera::pm1', 'Consultar asientos::pm2', 'Comprar tiquetes::pm3']],
            ['Agente de teatro',['Consultar cartelera::gm1', 'Consultar asientos::gm2', 'Vender tiquetes::gm3']],
            ['Administrador de teatro',['Definir nueva producción::tm1', 'Definir calendario producción::tm2', 'Definir precios producción::tm3',
                    'Cambiar estado de producción::tm4', 'Incluir agente autorizado::tm5']],
            ['Administrador del sistema', ['Agregar teatro::sm1', 'Agregar administrador teatro::sm2']]]

login_layout = [input_info('Username', 'lab_username','usuario_login'),
                [sg.Text('Password', key='lab_password'), sg.Input(key='password_login', password_char='*'), sg.Button('Login', key='blogin')]]

# --------------------------------- Layouts público --------------------------------- #
layout_pf1 = [input_info('Fecha inicio', 'pfi', 'pfie'),
              input_info('Fecha fin', 'pff', 'pffe')+[sg.Button('Consultar cartelera', key='pb1')]]

layout_pf2 = [input_info('Título', 'pttl1', 'pttl1e'), 
              input_info('Fecha presentación', 'pfp1', 'pfp1e'),
              input_info('Bloque', 'pbl1', 'pbl1e') + [sg.Button('Consultar disponibilidad', key='pb2')]]

layout_pf3 = [input_info('Título', 'pttl2', 'pttl2e'),
              input_info('Fecha', 'pfp2', 'pfp2e'),
              input_info('Bloque', 'pbl2', 'pbl2e'),
              input_info('Fila', 'pf', 'pfe'),
              input_info('Números', 'pn', 'pne') + [sg.Button('Comprar', key='pb3')]]

# --------------------------------- Layouts agentes --------------------------------- #
layout_gf1 = [input_info('Fecha inicio', 'gfi', 'gfie'),
            input_info('Fecha fin', 'gff', 'gffe')+[sg.Button('Consultar cartelera', key='gb1')]]

layout_gf2 = [input_info('Título', 'gttl1', 'gttl1e'), 
              input_info('Fecha presentación', 'gfp1', 'gfp1e'),
              input_info('Bloque', 'gbl1', 'gbl1e') + [sg.Button('Consultar disponibilidad', key='gb2')]]

layout_gf3 = [input_info('Título', 'gttl2', 'gttl2e'),
              input_info('Fecha', 'gfp2', 'gfp2e'),
              input_info('Bloque', 'gbl2', 'gbl2e'),
              input_info('Fila', 'gf', 'gfe'),
              input_info('Números', 'gn', 'gne'),
              [sg.Text('Forma pago', key='gpg'), sg.Combo(['Efectivo', 'Tarjeta'], key='gpge'), sg.Button('Vender', key='gb3')]]

# ------------------------------ Layouts admin. teatro ------------------------------ #
layout_tf1 = [input_info('Título', 'ttl1', 'ttl1e'),
              input_info('Tipo', 'ttip', 'ttipe'),
              input_info('Descripción', 'tdes', 'tdese') + [sg.Button('Crear Producción', key='tb1')]]

layout_tf2 = [input_info('Título', 'ttl2', 'ttl2e'),
              input_info('Fecha', 'tfec', 'tfece') + [sg.Button('Crear Presentación', key='tb2')]]

layout_tf3 = [input_info('Título', 'ttl3', 'ttl3e'),
              input_info('Bloque', 'tbl', 'tble'),
              input_info('Precio', 'tpr', 'tpre') + [sg.Button('Definir Precio', key='tb3')]]

layout_tf4 = [input_info('Título','ttl4', 'ttl4e'),
              input_info('Estado', 'tes', 'tese') + [sg.Button('Cambiar estado Presentación', key='tb4')]]

layout_tf5 = [input_info('Nombre', 'tnom', 'tnome'),
              input_info('Cedula', 'tced', 'tcede'),
              input_info('Fecha nacimiento', 'tfecn', 'tfecne'),
              [sg.Text('Sexo', key='tsx'), sg.Combo(['M', 'F'], key='tsxe')],
              input_info('Direccion', 'tdir', 'tdire'),
              input_info('Tel. Casa', 'ttc', 'ttce', (10,1)) + input_info('Celular', 'tcel', 'tcele',(10,1)) + input_info('Otro tel.', 'tot', 'tote', (10,1)),
              input_info('Email', 'tem', 'teme'),
              input_info('Usuario', 'tus', 'tuse'),
              input_info('Contraseña', 'tpass', 'tpasse') + [sg.Button('Registrar', key='tb5')]]

# ------------------------------ Layouts admin. sistema ------------------------------ #
layout_sf1 = [[sg.Text('Crear teatro')],
              input_info('Nombre', 'snomt1', 'snomt1e'),
              input_info('Telefono', 'stel', 'stele'),
              input_info('Website', 'sweb', 'swebe'),
              input_info('Tel. boletería', 'stelb', 'stelbe'),
              input_info('Email', 'sem', 'seme'),
              input_info('Capacidad', 'scap', 'scape') + [sg.Button('Crear teatro', key='sb1a')],
              [sg.HSeparator()],
              [sg.Text('Crear Bloque')],
              input_info('Teatro', 'stb', 'stbe'),
              input_info('Nombre Bloque', 'snomb', 'snombe') + [sg.Button('Crear bloque', key='sb1b')],
              [sg.HSeparator()],
              [sg.Text('Crear fila')],
              input_info('Teatro', 'stf', 'stfe'),
              input_info('Bloque', 'sbf', 'sbfe'),
              input_info('Letra', 'sl', 'sle'),
              input_info('Cantidad de asientos', 'scan', 'scane') + [sg.Button('Crear fila', key='sb1c')]]

layout_sf2 = [input_info('Nombre', 'snom', 'snome'),
              input_info('Cedula', 'sced', 'scede'),
              input_info('Teatro', 'st', 'ste'),
              input_info('Fecha nacimiento', 'sfec', 'sfece'),
              [sg.Text('Sexo', key='ssx'), sg.Combo(['M', 'F'], key='ssxe')],
              input_info('Direccion', 'sdir', 'sdire'),
              input_info('Tel. Casa', 'stc', 'stce', (10,1)) + input_info('Celular', 'scel', 'scele',(10,1)) + input_info('Otro tel.', 'sot', 'sote', (10,1)),
              input_info('Email', 'sem2', 'sem2e'),
              input_info('Usuario', 'sus', 'suse'),
              input_info('Contraseña', 'spass', 'spasse') + [sg.Button('Registrar', key='sb2')]]


# ------------------------------------ Main layout ----------------------------------- #
layout = [[sg.Menu(menu_def)],
          [col(layout_pf1, 'pf1'), col(layout_pf2, 'pf2'), col(layout_pf3, 'pf3'),
          col(layout_gf1, 'gf1'), col(layout_gf2, 'gf2'), col(layout_gf3, 'gf3'),
          col(layout_tf1, 'tf1'), col(layout_tf2, 'tf2'), col(layout_tf3, 'tf3'), col(layout_tf4, 'tf4'), col(layout_tf5, 'tf5'),
          col(layout_sf1, 'sf1'), col(layout_sf2, 'sf2'),
          col(login_layout, 'login_frame') ]]


# ------------------------------------------------------------------ #
# ----------------------- Window definition ------------------------ #
# ------------------------------------------------------------------ #
main_window = sg.Window("", layout, size=screen, font=my_font)
    

# ------------------------------------------------------------------ #
# -------------------------- Main method --------------------------  #
# ------------------------------------------------------------------ #
if __name__ == '__main__':
    while True:
        event, values = main_window.read()
        if event == None:
            break
        if event in frames.keys():
            main_window[current_frame].update(visible=False)
            current_frame = frames[event][0]
            if frames[event][1] == current_fn:
                main_window[current_frame].update(visible=True)
            elif frames[event][1] == 0:
                main_window[current_frame].update(visible=True)
                username = ''
                password = ''
            else:
                main_window['login_frame'].update(visible=True)
                login_handler(current_frame)
                current_fn = frames[event][1]
        if event in buttons.keys():
            buttons[event](values, username, password)

    main_window.close()