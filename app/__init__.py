from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)
    return app


def auth():
    token = request.headers.get('Authorization')
    if token == 'my_secret_token':
        return True
    else:
        return False
    return None