from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb-service:27017/")
db = client["ecommerce"]

orders = db.orders

@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "Running"
    })

@app.route("/orders", methods=["POST"])
def create_order():

    data = request.json

    order = {
        "user_id": data["user_id"],
        "product_name": data["product_name"],
        "quantity": data["quantity"],
        "status": "Placed"
    }

    orders.insert_one(order)

    return jsonify({
        "message": "Order Created Successfully"
    })

@app.route("/orders", methods=["GET"])
def get_orders():

    order_list = []

    for order in orders.find({}, {"_id": 0}):
        order_list.append(order)

    return jsonify(order_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)