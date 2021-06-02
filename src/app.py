
from flask import Flask, request, render_template, url_for, redirect

from model.ooxx import OOXXGame

app = Flask(__name__)

game = OOXXGame() # 建立一個 game

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global game
    return render_template('index.html', board = game.board)

if __name__ == "__main__":
    app.run(debug=True)