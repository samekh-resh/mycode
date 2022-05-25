#!/usr/bin/python3
from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    if name.lower() == "samekh":
        return f"Hello {name}"
    else:
        return redirect(url_for("dada", summy=name)) # missing an ending )
        #return redirect("/loser/<name>")

#@app.route("/hello")
#def hello_name():
        #return f"Hello "

@app.route("/loser/<summy>")
def dada(summy):
 return "we don't know you...\"{summy}\""
    ## V2 STYLE STRING FORMATTER - return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name
     

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   #so are you saying tha I need to create an app.route for (/) along with (/hello) to get to that place? 


