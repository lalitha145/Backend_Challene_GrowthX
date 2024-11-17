from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.models.assignment import Assignment
from app import bcrypt

def register_user():
    data = request.json
    data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    user_id = User.create_user(data)
    if not user_id:
        return jsonify({"error": "Email already exists"}), 400
    return jsonify({"message": "User registered successfully", "id": user_id}), 201

def login_user():
    data = request.json
    user = User.find_by_email(data["email"])
    if not user or not bcrypt.check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity={"id": str(user["_id"]), "role": user["role"]})
    return jsonify({"token": token})

def upload_assignment():
    data = request.json
    data["userId"] = request.user["id"]  # From middleware
    assignment_id = Assignment.create_assignment(data)
    return jsonify({"message": "Assignment uploaded", "id": assignment_id}), 201
