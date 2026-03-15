from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)