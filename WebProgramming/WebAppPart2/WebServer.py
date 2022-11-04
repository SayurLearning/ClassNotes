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
    return f'Double of {num} is {str(num / 0)}'

@app.route('/emp')
def employee():
    emp = {"Name": "Kannan", "Id": 1254}
    return emp

@app.route('/employees')
def employees():
    e = [
        {"Name":           "Kannan", "Id": 1254},
        {"Name":      "Alagarsamy", "Id": 456 },
        {"Name":    "Kathiresh", "Id": 785 }
        ]
    return e

app.run(host='0.0.0.0')

