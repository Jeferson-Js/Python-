from flask import Flask, render_template, request, redirect

class Conta:
    def __init__(self, agencia,titular,saldo):
        self.agencia = agencia
        self.titular = titular
        self.saldo = saldo


conta1 = Conta(106, 'Jeferson', 1000)
conta2 = Conta(106, 'Jeferson', 1000)
conta3 = Conta(106, 'Jeferson', 1000)
conta4 = Conta(106, 'Jeferson', 1000)
conta5 = Conta(106, 'Jeferson', 1000)
conta6 = Conta(106, 'Jeferson', 1000)
conta7 = Conta(106, 'Jeferson', 1000)
lista = [conta1, conta2, conta3, conta4, conta5, conta6, conta7]


app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('teste.html', titulo='Usuarios do banco', constas=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Usuario')


@app.route('/criar', methods=['POST',])
def criar():
    agencia = request.form['agencia']
    titular = request.form['titular']
    saldo = request.form['saldo']
    dados = Conta(agencia, titular, saldo)
    lista.append(dados)
    return redirect('/')

@app.route('/planos')
def planos():
    return render_template('cards.html', titulo='Planos')

app.run(debug=True)