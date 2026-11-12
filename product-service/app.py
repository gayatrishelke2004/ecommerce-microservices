from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb-service:27017/")
db = client["ecommerce"]

products = db.products

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "Running"
    })

@app.route("/products", methods=["POST"])
def add_product():

    data = request.json

    product = {
        "name": data["name"],
        "category": data["category"],
        "price": data["price"]
    }

    products.insert_one(product)

    return jsonify({
        "message": "Product Added Successfully"
    })

@app.route("/products", methods=["GET"])
def get_products():

    product_list = []

    for product in products.find({}, {"_id": 0}):
        product_list.append(product)

    return jsonify(product_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
