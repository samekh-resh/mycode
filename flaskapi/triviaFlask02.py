#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
app = Flask(__name__)

html= """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the meaning of life, the universe, and everything?</p>
<img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>"""

@app.route("/correct/<resp>")
def success(resp):
    resp = int(resp)
    return render_template("trial02.html", correctAnswer = resp)

@app.route("/incorrect/<resp>")
def failure(resp):
    return render_template("trial02.html", incorrectAnswer = resp)

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm") and request.form.get("nm") == "42":
            answer = request.form.get("nm")
            return redirect(f"/correct/{answer}")
        else:
            answer = request.form.get("nm")
            return redirect(f"/incorrect/{answer}")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
