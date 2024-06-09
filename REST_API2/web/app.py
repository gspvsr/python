from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import os
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
Users = db["Users"]

class Register(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"]
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        Users.insert_one({
            "Username" : username,
            "password" : hashed_pw,
            "Sentence" : "",
            "Tokens" : 10  # Each user gets 10 tokens initially
        })
        retJSON = {
            "status" : 200,
            "msg" : "You have successfully connected to API"
        }   
        return jsonify(retJSON)

class Store(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]
        correct_pw = self.verifyPW(username, password)
        if not correct_pw:
            retJSON = {
                "status" : 302
            }
            return jsonify(retJSON)
        num_tokens = self.verifyTokens(username)
        if num_tokens <= 0:
            retJSON = {
                "status" : 301
            }
            return jsonify(retJSON)
        Users.update_one({
            "Username" : username
        },
        {
            "$set" : {
                "Sentence" : sentence,
                "Tokens" : num_tokens - 1
            } 
        })
        retJSON = {
            "status" : 200,
            "msg": "Sentence saved successfully"
        }
        return jsonify(retJSON)
    
    @staticmethod
    def verifyPW(username, password):
        user = Users.find_one({"Username": username})
        if user:
            hashed_pw = user["password"]
            if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
                return True
        return False

    @staticmethod
    def verifyTokens(username):
        user = Users.find_one({"Username": username})
        if user:
            return user["Tokens"]
        return 0

class Get(Resource):
    def get(self):
        postedData = request.get_json()
        Username = postedData["username"]
        password = postedData["password"]

        correct_pw = verifyPW(username, password)
        if not correct_pw:
            retJSON = {
                "status" : 302
            }
            return jsonify(retJSON)
        
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJSON = {
                "status" : 301
            }
            return jsonify(retJSON)

        sentence = users.find({
            "Username" : username
        })[0]["Sentence"]

        retJson = {
            "status" : 200,
            "sentence" : sentence
        }
        return jsonify(retJson)
    
  
api.add_resource(Register, "/register")
api.add_resource(Store, "/store")
api.add_resource(Get, "/Get")  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
