from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    db.init_app()
    db.app = app
    with app.test_request_context():
        from model import Model
        db.create_all()

    return app
