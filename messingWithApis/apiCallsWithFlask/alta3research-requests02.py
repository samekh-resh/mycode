#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import json# just incase I wanted to post these 

app= Flask(__name__)


dayData= {
        'monday' : { 'description': 'the start of the week', 'activities': 'breathe'},
        'tuesday' : { 'description': 'the day for tea', 'activities': 'make a cup of tea'},
        'wednesday' : { 'description': 'the whale\'s day', 'activities': 'take it easy'},
        'thursday' : { 'description': 'the new friday', 'activities': 'take a nice jog'},
        'friday' : { 'description': 'sweet release', 'activities': 'BAR HOPPING'},
        'saturday' : { 'description': 'one of two sacred rest days...', 'activities': 'naaaah we playing soccer'},
        'sunday' : { 'description': 'two of two sacred rest days...', 'activities': 'naaaah we\'re baking all day'}
        }
@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(dayData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2227)
