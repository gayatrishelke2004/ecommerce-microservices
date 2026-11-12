from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb-service:27017/")
db = client["ecommerce"]

@app.route("/")
def home():
    return jsonify({
        "service": "Recommendation Service",
        "status": "Running"
    })

@app.route("/recommend/<category>", methods=["GET"])
def recommend(category):

    recommendations = {
        "Mobile": ["AirPods Pro", "20W Charger", "Power Bank"],
        "Laptop": ["Wireless Mouse", "Mechanical Keyboard", "Laptop Bag"],
        "TV": ["Sound Bar", "Wall Mount", "HDMI Cable"],
        "Gaming": ["Gaming Mouse", "Gaming Headset", "RGB Keyboard"]
    }

    return jsonify({
        "category": category,
        "recommendations": recommendations.get(
            category,
            ["No Recommendations Available"]
        )
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)