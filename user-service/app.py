from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb-service:27017/")
db = client["ecommerce"]

users = db.users

@app.route("/register", methods=["POST"])
def register():

    data = request.json

    users.insert_one({
        "name": data["name"],
        "email": data["email"]
    })

    return jsonify({"message":"User Registered"})

@app.route("/users")
def get_users():

    result = []

    for user in users.find({}, {"_id":0}):
        result.append(user)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)