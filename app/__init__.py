from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import urandom
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY=urandom(24),
    static_folder='static',
    template_folder='templates',
    static_url_path = "templates",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ))

from app import views

