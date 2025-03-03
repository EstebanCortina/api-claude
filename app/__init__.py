from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.api.v1 import bp as api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    return app

from app import models