#!/usr/bin/env python

#import necessary libraries
#pip install flask
from flask import Flask, json,render_template,request,redirect,url_for
import os
import urllib.parse as urlparse
from urllib.parse import parse_qs

#create instamce of the application
#export FLASK_APP=flask-app

app  = Flask(__name__)

#decorator
@app.route("/")
def hello():
    return "<p>Nobel Prize</p>"

#decorator
@app.route("/all")
def nobel():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))

    #render template is always looking in tempate folder
    return render_template('index.html',data=data_json)


@app.route("/<year>",methods=['GET','POST'])
def nobel_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json['prizes']
    year = request.view_args['year']
    if request.method == 'GET':
        output_data = [x for x in data if x['year']==year]
        
        #render template is always looking in tempate folder
        return render_template('nobel.html',data=output_data)
    elif request.method == 'POST':
       	category = request.form["category"]
        chemistry = request.form["chemistry"]
        id = request.form["id"]
        firstname = request.form["firstname"]
        surname = request.form["surname"]
        motivation = request.form["motivation"]
        share = request.form["share"]
        nobel_yr= { "year":year,
                    "category":category,
                    "chemistry":chemistry,
                    "laureates":[{"id":id,
                                "firstname":firstname,
                                "surname":surname,
                                "motivation":motivation,
                                "share":share
                                 }]
                    }
        with open('./static/nobel.json','r+') as file:
          # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["prizes"].append(nobel_yr)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
    
        #return render_template('index.html',data=category+chemistry)    
        return redirect(url_for("nobel_year",year=year))
      


if __name__ == "__main__":
    app.run(debug=True)

