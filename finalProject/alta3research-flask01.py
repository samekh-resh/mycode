#!/usr/bin/env python3
from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
import requests
from flask import redirect
from flask import url_for
from flask import jsonify


#so using with/as to read the file then using json.load to read it as json then add it in with the jsonify() function 
#solution for taking the code from the endpoint in the other file and reading it. 
app = Flask(__name__)

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
URL= "http://127.0.0.1:2227/"

@app.route("/jsondata")
def showjson():
    dayInfo = requests.get(URL).json()
    print(dayInfo)
    #return jsonify(days)
    return dayInfo


@app.route("/today/<nameIn>/<dayIn>")
def showDay(nameIn, dayIn):
    days = showjson()
    
    print(days[dayIn]['description'])
    print(days[dayIn]['activities'])
    descriptionOfDay = days[dayIn]['description']
    activityForDay = days[dayIn]['activities']
    return render_template("weekDayTemplate.html", name  = nameIn, day = dayIn, description = descriptionOfDay, activity = activityForDay)


#entry point for our users and it's going to render the template that asks for name
@app.route("/")
def index():
    return render_template("loginTemplate.html")

@app.route("/sendInfo", methods = ["POST"])
def getName():
    if request.method == "POST":
        if request.form.get("name") and request.form.get("nm"):
            userName = request.form.get("name")
            userDay = request.form.get("nm").lower()
            return redirect(f"/today/{userName}/{userDay}")
        else:
            userName = "no name input" 
            userDay = "someday"
            return redirect(f"/today/{userName}/{userDay}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
