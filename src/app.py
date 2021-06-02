
from flask import Flask, request, render_template, url_for, redirect

from model.ooxx import OOXXGame

app = Flask(__name__)

game = OOXXGame() # 建立一個 game

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global game

    value = request.form.get('button')
    if value is not None:
        game.clickBoard(int(value))

    button_dict_list = []
    count = len(game.board)
    for index in range(count):
        x = index % 3
        y = (index - x) / 3
        dict = {
            "left": f"{ 50 * x + 100 }px",
            "top": f"{ 50 * y + 100}px",
            "symbol": game.board[index],
            "id": index,
        }
        button_dict_list.append(dict)

    return render_template('index.html', button_dict_list = button_dict_list)

if __name__ == "__main__":
    app.run(debug=True)