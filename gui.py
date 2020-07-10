import PySimpleGUI as sg

# ------------------------------------------------------------------ #                                 |    Público     |  'p..'
# --------------------------- Variables ---------------------------- #                                 | Agente teatro  |  'g..'
# ------------------------------------------------------------------ #                                 | Admin. teatro  |  't..'
#                                                                    #                                 | Admin. sistema |  's..'

sg.theme('light grey 6')
screen = (1000,800)
my_font = ('Arial', 14)

current_frame = 'pf1'
frames = {'Consultar cartelera::pm1':'pf1', 'Consultar asientos::pm2':'pf2', 'Comprar tiquetes::pm3':'pf3',
          'Consultar cartelera::gm1':'gf1', 'Consultar asientos::gm2':'gf2', 'Vender tiquetes::gm3':'gf3',
          'Definir nueva producción::tm1':'tf1', 'Definir calendario producción::tm2':'tf2', 'Definir precios producción::tm3':'tf3',
                    'Cambiar estado de producción::tm4':'tf4', 'Incluir agente autorizado::tm5':'tf5',
          'Agregar teatro::sm1':'sf1', 'Agregar administrador teatro::sm2':'sf2' }
buttons = {}

# ------------------------------------------------------------------ #
# ---------------- Functions for layout definition ----------------- #
# ------------------------------------------------------------------ #
def input_info(lab, inKey):
    # falta meterle key al text
    return [sg.Text(lab), sg.Input(key=inKey)]

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

layout_pf1 = [input_info('Fecha', '-fecha_consulta-')]

layout_pf2 = [input_info('Título', '-titulo_obra-')]

layout_pf3 = [input_info('Título2', '-titulo_2-'),
                input_info('Bloque', '-nombre_bloque-')]

layout_gf1 = [[sg.Text('gf1')]]
layout_gf2 = [[sg.Text('gf2')]]
layout_gf3 = [[sg.Text('gf3')]]

layout_tf1 = [[sg.Text('tf1')]]
layout_tf2 = [[sg.Text('tf2')]]
layout_tf3 = [[sg.Text('tf3')]]
layout_tf4 = [[sg.Text('tf4')]]
layout_tf5 = [[sg.Text('tf5')]]

layout_sf1 = [[sg.Text('sf1')]]
layout_sf2 = [[sg.Text('sf2')]]


layout = [[sg.Menu(menu_def)],
          [col(layout_pf1, 'pf1'), col(layout_pf2, 'pf2'), col(layout_pf3, 'pf3'),
          col(layout_gf1, 'gf1'), col(layout_gf2, 'gf2'), col(layout_gf3, 'gf3'),
          col(layout_tf1, 'tf1'), col(layout_tf2, 'tf2'), col(layout_tf3, 'tf3'), col(layout_tf4, 'tf4'), col(layout_tf5, 'tf5'),
          col(layout_sf1, 'sf1'), col(layout_sf2, 'sf2') ]]


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
        # main_window['-titulo_obra-'].update(event)
        if event == None:
            break
        if event in frames.keys():
            main_window[current_frame].update(visible=False)
            current_frame = frames[event]
            main_window[current_frame].update(visible=True)


    main_window.close()

    '''
    def hello():
        print('hello')

    def goodbye():
        print('goodbye')
    
    d = {'h':hello, 'g':goodbye}

    d['g']()
    '''