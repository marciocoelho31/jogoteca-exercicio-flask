from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('River Raid', 'Ação', 'Odyssey')
    jogo3 = Jogo('Counter Strike', 'Tiro', 'Playstation')

    lista_jogos = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='Jogos', jogos = lista_jogos)

app.run()