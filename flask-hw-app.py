#!/usr/bin/env python

#import necessary libraries
#pip install flask
from flask import Flask, json,render_template,request
import os

#create instamce of the application
#export FLASK_APP=flask-app

app  = Flask(__name__)


#decorator
@app.route("/")
def nobel():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))

    #render template is always looking in tempate folder
    return render_template('index.html',data=data_json)


@app.route("/<year>")
def nobel_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json['prizes']
    year = request.view_args['year']
    output_data = [x for x in data if x['year']==year]
    #render template is always looking in tempate folder
    return render_template('index.html',data=output_data)

if __name__ == "__main__":
    app.run(debug=True)


