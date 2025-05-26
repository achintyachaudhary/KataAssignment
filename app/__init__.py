from flask import Flask
from .config import Config
from .routes.cart import cart_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Register blueprint
    app.register_blueprint(cart_bp, url_prefix="/cart")
    return app
