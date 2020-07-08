import PySimpleGUI as sg
from constants import IConstants

# sg.theme('dark teal')
# sg.theme_previewer()
constants = IConstants()
sg.theme('light grey 6')
# sg.CalendarButton para seleccionar fechas promete

'''Usar tabs o w'''

def input_info(lab, inKey):
    return [sg.Text(lab), sg.Input(key=inKey)]

# Layout
menu_def = [['File', ['opt1', 'opt2']], 
            ['Edit'], 
            ['Other option']]

frame_layout = [input_info('Título', '-titulo_obra-')]

layout = [[sg.Menu(menu_def)],
            [sg.Frame('', frame_layout, size=constants.screen)]
            ]

# Window creation
window = sg.Window('Demo', layout, size=constants.screen, font=('Arial', 14))

# Event loop
while True:
    event, value = window.read()
    print(event)
    if event == None:
        break

# End
window.close()

# menu app https://www.youtube.com/watch?v=xmG53Fwynps&list=PLl8dD0doyrvFfzzniWS7FXrZefWWExJ2e&index=14 