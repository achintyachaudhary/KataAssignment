from flask import Blueprint, jsonify
from flask import request

from app.services.cart import calculate_product_price

cart_bp = Blueprint("auth", __name__)


@cart_bp.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()
    price = calculate_product_price(data['products'])
    return jsonify({
        "product": data['products'],
        "fees": price
    }), 200
