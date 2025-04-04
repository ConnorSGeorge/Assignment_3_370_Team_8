from pymongo import MongoClient

# Sample data similar to what is in userService.py
users_data = [
    {"id": "1", "name": "John Doe", "email": "john.doe@example.com"},
    {"id": "2", "name": "Jane Smith", "email": "jane.smith@example.com"},
    {"id": "3", "name": "Alice Johnson", "email": "alice.johnson@example.com"}
]

# Sample data for orders
orders_data = [
    {"order_id": "101", "user_id": "1", "product_id": "1001", "quantity": 1},
    {"order_id": "102", "user_id": "2", "product_id": "1002", "quantity": 2},
    {"order_id": "103", "user_id": "3", "product_id": "1003", "quantity": 1},
    {"order_id": "104", "user_id": "1", "product_id": "1003", "quantity": 3}
]

def populate_db():
    # Connect to MongoDB server
    client = MongoClient('localhost', 27017)
    
    # Create or switch to 'storedb' database
    db = client.storedb
    
    # Populate 'users' collection
    users_collection = db.users
    users_collection.delete_many({})
    users_collection.insert_many(users_data)
    
    # Populate 'orders' collection
    orders_collection = db.orders
    orders_collection.delete_many({})
    orders_collection.insert_many(orders_data)
    
    print("Database populated successfully!")

if __name__ == "__main__":
    populate_db()
