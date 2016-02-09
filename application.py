from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<menu>')
def board():
    return render_template('list.html')


@app.route('/<menu>/<article_no>')
def hello_world2():
    return render_template('show.html')


if __name__ == '__main__':
    app.run()
