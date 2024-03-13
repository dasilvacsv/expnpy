# app.py
from flask import Flask
from views.home import home
from routes import api
from models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # replace with your database path
    db.init_app(app)
    app.register_blueprint(home)
    app.register_blueprint(api, url_prefix='/api')
    return app