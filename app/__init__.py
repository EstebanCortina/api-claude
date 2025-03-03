from flask import Flask
from app.config.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    from app.api.v1 import bp as api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    return app

# Import models so they're available to import elsewhere
from app import models