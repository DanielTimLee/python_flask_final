from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['localhost'] = 'mysql://root:daniel@localhost/flask'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<menu>')
def board(menu):
    return "hi"


@app.route('/<menu>/<article_no>')
def hello_world2():
    return render_template('show.html')


if __name__ == '__main__':
    app.run(debug=True)
