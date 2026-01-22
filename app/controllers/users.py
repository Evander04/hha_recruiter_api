from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])

@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    username = data.get("username")
    email = data.get("email")
    pwd = data.get("password")

    if not username or not email:
        return jsonify({"error": "username and email are required"}), 400

    user = User(username=username, email=email)
    user.set_password(pwd)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created", "id": user.id}), 201
