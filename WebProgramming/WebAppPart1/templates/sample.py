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
    return render_template('test/index.html')


@app.route('/text')
def home():
    return render_template('employee.txt')


app.run()
