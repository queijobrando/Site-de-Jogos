from flask import Flask, render_template, request, redirect

class Game:#classe do jogo
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Game('Tetris', 'Puzzle', 'Atari')
jogo2 = Game('God of War', 'Rack n Slash', 'PS2')

lista = [jogo1, jogo2]  #lista do jogo

#-----------------------------------------------------#
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo_site='Site de Jogos', titulo='Jogos', games = lista)

@app.route('/newgame') #pagina inserir novo jogo
def newgame():
    return render_template('newgame.html', titulo_site='Site de Jogos', titulo='Novo Jogo')

@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('nome')
    category = request.form.get('categoria')
    console = request.form.get('console')
    jogo = Game(name, category, console) #cria um jogo novo
    lista.append(jogo) #adiciona na lista de jogos
    return redirect('/') #redireciona para a pagina inicial
    
if __name__ == '__main__':
    app.run(debug=True)