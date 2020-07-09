import PySimpleGUI as sg

# ------------------------------------------------------------------ #
# --------------------------- Variables ---------------------------- #
# ------------------------------------------------------------------ #
sg.theme('light grey 6')
screen = (1000,800)
my_font = ('Arial', 14)


# ------------------------------------------------------------------ #
# ---------------- Functions for layout definition ----------------- #
# ------------------------------------------------------------------ #
def input_info(lab, inKey):
    return [sg.Text(lab), sg.Input(key=inKey)]


# ------------------------------------------------------------------ #
# --------------------------- Layouts ------------------------------ #
# ------------------------------------------------------------------ #
menu_def = [['Clientes', 'comprar'],
            ['Agente de teatro'],
            ['Administrador de teatro'],
            ['Administrador del sistema']]

frame_layout = [input_info('Título', '-titulo_obra-')]

layout = [[sg.Menu(menu_def)],
            [sg.Frame('', frame_layout, size=screen, key='-MyFrame-')]
            ]

# ------------------------------------------------------------------ #
# ----------------------- Window definition ------------------------ #
# ------------------------------------------------------------------ #
main_window = sg.Window("", layout, size=screen, font=my_font)


# ------------------------------------------------------------------ #
# ---------------- Functions for window management ----------------- #
# ------------------------------------------------------------------ #

def client_window_run():
    while True:
        break

def theatre_agent_window_run():
    while True:
        break

def theatre_admin_window_run():
    while True:
        break

def sys_admin_window_run():
    while True:
        break

def main_window_run():
    while True:
        event, value = main_window.read()
        main_window['-titulo_obra-'].update(event)
        if event == None:
            break

# ------------------------------------------------------------------ #
# -------------------------- Main method --------------------------  #
# ------------------------------------------------------------------ #
if __name__ == '__main__':
    main_window_run()
    main_window.close()