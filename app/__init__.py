from flask import Flask
import os
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)

    # Choose config by APP_ENV (not FLASK_ENV)
    app_env = os.getenv("APP_ENV", "development").lower()
    config_map = {
        "development": "app.config.dev.DevConfig",
        "production": "app.config.prod.ProdConfig",
    }
    app.config.from_object(config_map.get(app_env, "app.config.dev.DevConfig"))

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.controllers.health import health_bp
    from app.controllers.users import users_bp
    from app.controllers.clients import clients_bp

    app.register_blueprint(health_bp, url_prefix="/api/health")
    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(clients_bp, url_prefix="/api/clients")

    return app
