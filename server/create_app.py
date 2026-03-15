import os

from flask import Flask
from flask_migrate import Migrate

from server.models import db


def create_app():
    app = Flask(__name__, static_folder="../client/www", static_url_path="")
    _db_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "db"))
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{_db_dir}/app.db"
    db.init_app(app)
    Migrate(app, db, directory=f"{_db_dir}/migrations")
    return app