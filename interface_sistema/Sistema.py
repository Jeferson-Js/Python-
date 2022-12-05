import PySimpleGUI as sg

sg.theme('DarkBlue4')

layout = [
    [sg.Text('Response the user')],
    [sg.Input(key='user', size=(30, 20))],
    [sg.Button('Response')],
    [sg.Text(key='mensage')]
]

window = sg.Window('Response the user', layout)

while True:

    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Response':
        usuario = values['user']
        if usuario == values['user']:
            window['mensage'].update('Seja bem vindo ao mundo python, {}'.format(usuario))
window.close()