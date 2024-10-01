from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    # Registrar los Blueprints
    from .api.routes import routes
    app.register_blueprint(routes)

    return app
