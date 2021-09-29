'''
created by : Prakash R

'''


from flask import Flask,render_template, jsonify, request, url_for
import random
import json
import pymongo
from pymongo import MongoClient
from bson import json_util
from flask import Markup
import os


app = Flask(__name__)
PORT = 3000

MONGO_URI= os.environ.get('MONGO_URI')

cluster = MongoClient(MONGO_URI)

db = cluster["data"]
user_col = db["user_details"]


@app.route("/", methods=["GET"])
def startpy():

    return render_template("add-user-personal-details.html") 

def get_user_id(user_id):

    user_id = {
        "user_id" : int(user_id)
    }

    user_id_obj = user_col.find_one(user_id)

    return user_id_obj

def get_last_user_id():

    last_user_id      = user_col.find().sort([('user_id', -1)]).limit(1)

    try:
        last_user_id = last_user_id[0]['user_id']
    except Exception as err:
      
        last_user_id = 0

    return last_user_id


@app.route("/data/submit", methods=["POST"])
def submit():

        last_user_id = get_last_user_id()

        current_user_id = last_user_id + 1

        name     = request.form.get("name")
        surname    = request.form.get("surname")
        bdate    = request.form.get("bdate")
        street     = request.form.get("street")
        city    = request.form.get("city")
        postcode    = request.form.get("postcode")
        country     = request.form.get("country")
        email     = request.form.get("email")
        phone     = request.form.get("phone")
        mobile     = request.form.get("mobile")

        result   = {
            "user_id"  : current_user_id ,
            "Name"     : name ,
            "Surname"  : surname , 
            "Birthdate": bdate , 
            "Street"   : street,
            "City"     : city,
            "Postcode" : postcode ,
            "Country"  : country ,
            "Email"    : email , 
            "Phone"    : phone , 
            "Mobile"   : mobile
           
        }

        user_col.insert_one(result)
    
        return render_template("data.html")

@app.route('/all_details',methods=["GET"])
def all_details():
    
    user_details =[]
    for user in user_col.find():
        user_id     = user["user_id"]
        Name        = user['Name']
        Surname     = user['Surname']
        Birthdate   = user['Birthdate']
        Street      = user['Street']
        City        = user['City']
        Postcode    = user['Postcode']
        Country     = user['Country']
        Email       = user['Email']
        Phone       = user['Phone']
        Mobile      = user['Mobile']


        result = {
            'Name'      : Name,
            'Surname'   : Surname,
            'Birthdate' : Birthdate,
            'Street'    : Street,
            'City'      : City,
            'Postcode'  : Postcode,
            'Country'   : Country,
            'Email'     : Email,
            'Phone'     : Phone,
            'Mobile'    : Mobile

        }
        user_details.append(result)
    # print(details)
    return render_template("user_details.html",result = user_details)

@app.route("/data/edit", methods=["GET","POST"])
def view():

    data = user_col.find()




    


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)








