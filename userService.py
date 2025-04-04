from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

class UserService:
    def __init__(self):
        # Connect to MongoDB server
        self.client = MongoClient('localhost', 27017)
        # Switch to 'storedb' database
        self.db = self.client.storedb
        # Switch to 'users' collection
        self.users_collection = self.db.users

    def get_user(self, user_id):
        # Fetch user from the 'users' collection
        user = self.users_collection.find_one({"id": user_id}, {'_id': 0})
        return user

user_service = UserService()

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
