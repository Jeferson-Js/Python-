import PySimpleGUI as sg

sg.theme('python')

layout = [
    [sg.Text('First Value'), sg.Input(key='FirstValue', size=(20,1))],
    [sg.Text('Second Value'), sg.Input(key='SecondValue', size=(20,1))],
    [sg.Button('Soma')],
    [sg.Text(key="mesage")]
]
window = sg.Window('Adding 2 numbers', layout)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Soma':
        value1 = int(values['FirstValue'])
        value2 = int(values['SecondValue'])
        adding = (value1 + value2)
        window['mesage'].update('The sum between {} and {} is {}! '.format(value1, value2, adding))

window.close()