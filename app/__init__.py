from flask import Flask
from os import urandom

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY=urandom(24),
    static_folder='static',
    template_folder='templates',
    static_url_path = "templates",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ))

from app import views

