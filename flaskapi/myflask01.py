#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

#flask constructor takes the name of current module (__name__) as argument
app = Flask(__name__)

name = "samekh"
#clients should send a get request, what we send back is hello world 
@app.route('/')
def hellerWerld():
    return "Heller Werld"

#@app.route("/hello")
#def hello_world():
#    return "hello world from a different route"


@app.route('/samekh')
def helloMekh():
    return name + ", hi there my good one."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

