from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv(
    "MONGO_URI",
    "mongodb://mongodb-service:27017/"
)

client = MongoClient(mongo_uri)
db = client["ecommerce"]
products_collection = db["products"]


@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "Running"
    })


@app.route("/products", methods=["POST"])
def add_product():

    data = request.get_json()

    product = {
        "name": data["name"],
        "category": data["category"],
        "price": data["price"]
    }

    products_collection.insert_one(product)

    return jsonify({
        "message": "Product added successfully"
    }), 201


@app.route("/products", methods=["GET"])
def get_products():

    products = []

    for product in products_collection.find({}, {"_id": 0}):
        products.append(product)

    return jsonify(products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
