from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# config

app = Flask(__name__)
app.config['SQLALCHEMY-URL'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User():
    id = db.Column(db.INTEGER, primary_key=True)
    first_name = db.Column(db.VARCHAR, unique=True)
    last_name = db.Column(db.VARCHAR, nullable=True)
    age = db.Column(db.INTEGER)

    def __repr__(self):
        return f" User({self.id}-{self.first_name})"
