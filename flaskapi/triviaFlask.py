#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

#@app.route("/correct/<word>")
@app.route("/correct")
def correctWord():
    return "that answer is correct"
    #return f"{word} that is correct : )"

@app.route("/userAttempt/<answer>")
def userAnswer(answer):
    if answer == "blue":
        return redirect(url_for("correct"))
    if answer !=  "blue":
        return render_template("triviaFlask.html")


@app.route("/")
def start():
    return render_template("triviaFlask.html")


@app.route("/userAnswer", methods=["POST", "GET"])
def showAnswer():
    if request.method == "POST":
        if request.form.get("answer"): #if nm was assigned via the post
            userAnswer = request.form.get("answer")
        else: #if the user sent a post without an answer
            user = "chartruese"
    elif request.method == "GET":
        if request.args.get("answer"): #if answer was assigned as a parameter=value
            userAnswer = request.args.get("answer") #pulsl answer from lovcalhost:2224/userAnswer?answer=whatever
        else: #if nm was not passed
            userAnswer = "chartruese"
    return redirect(url_for("userAttempt", answer= userAnswer))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) #runs the application
