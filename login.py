import PySimpleGUI as sg

sg.theme('lightGreen2')

layout = [
    [sg.Text('UserName'),sg.Input(key='user', size=(30,30))],
    [sg.Text('PassWord'), sg.Input(key='password', password_char="*", size=(30,30))],
    [sg.Button('Logar', size=(30, 1))],
    [sg.Text(key='mensagem')]
]

window = sg.Window('Sistema de login', layout)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Logar':
        password_correct = "123456"
        user_correct = values['user']
    if values['user'] == user_correct and values['password'] == password_correct:
        window['mensagem'].update('Usuario logado com sucesso!'.format(user_correct))
    else:
        window['mensagem'].update('Usuario ou senha invalidos!')

window.close()