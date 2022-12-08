from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categora, console):
        self.nome = nome
        self.categoria = categora
        self.console = console

jogo1 = Jogo('Super Mario', 'Aventura', 'Super Nitendo')
jogo2 = Jogo('Homen Aranha', 'Aventura', 'Playstation 1')
jogo3 = Jogo('Mortal Combat', 'Luta', 'Playstation 2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST',])
def criar():
        nome = request.form['nome']
        categoria = request.form['categoria']
        console = request.form['console']
        jogo = Jogo(nome, categoria,console)
        lista.append(jogo)
        return redirect('/')

app.run(debug=True)
