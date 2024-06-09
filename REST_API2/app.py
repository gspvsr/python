# - Registration of a user 0 tokens
# - Each user gets 10 tokens
# - Store a sentence on our database  for 1 token
# - Retreive his stored sentence on out database for 1 token

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import os
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentancesDatabase
Users = db["Users"]

class Register(Resource):
    def post(self):
        
        
        #step 1: is to get the posted data by user
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        #hash(123xyz +salt) = jskshsklsahlksjhdljh
        hashed_pw = bcrypt.hashpw(password.enclode('utf8'), bcrypt.gensalt())

        # store username and pw into the SentanceDatabase
        Users.insert_one({
            "Username" : username,
            "password" : hashpw,
            "Sentence" : "",
            "Tokens" :6
        })

        retJSON = {
            "status" : 200,
            "msg" : "you have successfully connected to API"
        }   
        return jsonify(retJSON)
    
    def verifyPW(username, password):
        hashed_pw = Users.find({
            "Username" : username
        })[(0)["Password"]]

        if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
            return True
        else:
            return False

    def verifyTokens(username):
        tokens = Users.find({
            "Username" : username
        })[(0)["Tokens"]]
        return tokens
    
class Store(Resource):
    def post(self):
        # step1: Get the posted data
        postedData = request.get_json()

        # step2: read the data.
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData[["sentence"]]

        # step3: verify username and password match.
        correct_pw = verifyPW(username, password)

        if not correct_pw:
            retJSON = {
                "Status" : 302
            }
            return jsonify(retJson)

        # step4: verify if the user has enough tokens.
        num_tokens = countTokens(username)
        if num_tokens <=0:
            retJson = {
                "status" : 301
            }
            return jsonify(retJson)
        # step5: store sentence take one away return 200

        Users.update_one({
            "Username" : username
        },
        {
            "$set" : {
                "Sentence" : sentence,
                "Tokens" : num_tokens - 1
            } 

        })

        retJson = {
            "status" : 200,
            "msg": "Sentence saved successfully"
        }
        return jsonify(retJson)
        
api.add_resource(Register, "/register")
api.add_resource(Store, "/store")

@app.route('/')
def gsp_world():
    return "hi gsp how are you"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

