from flask import current_app
from app import mongo

class User:
    @staticmethod
    def create_user(data):
        users = mongo.db.users
        if users.find_one({"email": data["email"]}):
            return None  # Email already exists
        user_id = users.insert_one(data).inserted_id
        return str(user_id)

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email": email})
