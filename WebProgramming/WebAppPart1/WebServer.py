from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return '<h1>Hi, Welcome to Sayur Tech!!</h1><br/><a href="https://gmail.com">My Email</a>'

@app.route('/email')
def my_email():
    return '<a href="https://gmail.com">My Email</a>'


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/python')
def python():
    return render_template('sample.py')

@app.route('/greet/<fname>/<lname>')
def greet_me(fname, lname):
    return f'Hello {fname} {lname}! Welcome to Sayur Tech.'

@app.route('/double/<int:num>')
def double(num):
    return f'Double of {num} is {str(num * 2)}'


app.run()
