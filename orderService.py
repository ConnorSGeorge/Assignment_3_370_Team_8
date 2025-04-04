from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB server
client = MongoClient('localhost', 27017)
db = client.storedb
orders_collection = db.orders

@app.route('/orders', methods=['GET'])
def get_orders():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    # Fetch orders for the given user_id
    orders = list(orders_collection.find({"user_id": user_id}, {"_id": 0}))
    return jsonify(orders)

if __name__ == '__main__':
    app.run(port=5001)
