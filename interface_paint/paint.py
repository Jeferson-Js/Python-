import PySimpleGUI as sg

sg.theme('python')

layout = [
    [sg.Text('Paint the wall')],
    [sg.Text('Largura:'), sg.Input(key="largura", size=(25, 1))],
    [sg.Text('Altura:'), sg.Input(key="altura", size=(25, 1))],
    [sg.Button('Calcular')],
    [sg.Text(key="mesage")]
]

window = sg.Window('Pintando uma parede', layout)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Calcular':
        largura = float(values['largura'])
        altura = float(values['altura'])
        area = (largura * altura)
        tinta = area / 2
    if largura == values['largura']:
        window['mesage'].update('Sua parede tem a dimensão de {} x {} e sua area é  de {}m².'.format(largura, altura, area))
        print('quanto de tinta'.format(tinta))
    altura == values['altura']
    window['mesage'].update('Para pintar essa parede você precisara de {} litros de tinta.'.format(tinta))
window.close()
