from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/<string:name>')  
#def hello(name):
#    return f"<h1> Hello, {name}</h1>"
def hello():
    name = request.form.get('name')
    return render_template('hello.html', name=name)
