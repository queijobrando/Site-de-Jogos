from flask import Flask, render_template

class Game:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/')
def home():
    jogo1 = Game('Tetris', 'Puzzle', 'Atari')
    jogo2 = Game('God of War', 'Rack n Slash', 'PS2')

    lista = [jogo1, jogo2]
    return render_template('index.html', titulo_site='Jogos', games = lista)
    
if __name__ == '__main__':
    app.run(debug=True)