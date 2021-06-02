
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True)