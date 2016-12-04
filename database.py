from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def create_app(app):
    db.init_app(app)
    db.app = app

    db.create_all()

