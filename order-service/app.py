from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql-service",
    user="root",
    password="root123",
    database="ecommerce"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_name VARCHAR(255),
    quantity INT,
    status VARCHAR(50)
)
""")

db.commit()


@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "Running"
    })


@app.route("/orders", methods=["POST"])
def create_order():

    data = request.json

    sql = """
    INSERT INTO orders
    (user_id, product_name, quantity, status)
    VALUES (%s,%s,%s,%s)
    """

    values = (
        data["user_id"],
        data["product_name"],
        data["quantity"],
        "PLACED"
    )

    cursor.execute(sql, values)
    db.commit()

    return jsonify({
        "message": "Order Created Successfully"
    })


@app.route("/orders", methods=["GET"])
def get_orders():

    cursor.execute(
        "SELECT user_id, product_name, quantity, status FROM orders"
    )

    rows = cursor.fetchall()

    result = []

    for row in rows:

        result.append({
            "user_id": row[0],
            "product_name": row[1],
            "quantity": row[2],
            "status": row[3]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
