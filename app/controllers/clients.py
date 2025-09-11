from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.client import Client

clients_bp = Blueprint("clients", __name__)

@clients_bp.route("/", methods=["GET"])
def list_clients():
    clients = Client.query.all()
    return jsonify([{"id": c.id, "company_name": c.company_name, "contact_email": c.contact_email} for c in clients])

@clients_bp.route("/", methods=["POST"])
def create_client():
    data = request.get_json() or {}
    company_name = data.get("company_name")
    contact_email = data.get("contact_email")
    if not company_name or not contact_email:
        return jsonify({"error": "company_name and contact_email are required"}), 400

    client = Client(company_name=company_name, contact_email=contact_email)
    db.session.add(client)
    db.session.commit()
    return jsonify({"message": "Client created", "id": client.id}), 201
