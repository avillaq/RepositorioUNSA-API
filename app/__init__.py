from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    # Registrar los Blueprints
    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
