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

db = cluster[""]
col = db[""]

app.config["POST"] = os.environ.get('MONGO_URI')

@app.route("/", methods=["GET"])
def startpy():

    return render_template("index.html") 

def get_user_id(user_id):

    user_id = {
        "user_id" : int(user_id)
    }

    user_id_obj = col.find_one(user_id)

    return user_id_obj

def get_last_user_id():

    last_user_id      = col.find().sort([('user_id', -1)]).limit(1)

    try:
        last_user_id = last_user_id[0]['user_id']
    except Exception as err:
      
        last_user_id = 0

    return last_user_id

@app.route("/submit", methods=["POST"])
def submit(request_json):
    user_id = request_json["user_id"]
    name     = request.form.get("name")
    email    = request.form.get("email")
    regno    = request.form.get("regno")
    dept     = request.form.get("dept")
    year     = request.form.get("year")

    result   = {
        "user_id"  : user_id ,
        "Name"     : name ,
        "Email"    : email , 
        "Regno"    : regno , 
        "Dept"     : dept,
        "year"     : year
    }
    





if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)








