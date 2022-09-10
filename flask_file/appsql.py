from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    first_name = db.Column(db.VARCHAR, unique=True)
    last_name = db.Column(db.VARCHAR, nullable=True)
    age = db.Column(db.INTEGER)

    def __repr__(self):
        return f" User({self.id}-{self.first_name})"


@app.route('/home1')
def showing_objects():
    users = User.query.all()
    return render_template('home1.html', users=users)


@app.route('/<user_id>')
def detail(user_id):
    user = User.query.get(user_id)
    return render_template('detail.html', user=user)


# create database
"""
.in terminal :
 from appsql import db
 db.create_all()
 #database is created
 ____________________
 # add value in database
 example :
 from appsql import User 
 user1 = User(first_name = "reza" , last_name = "amin" , age = 22)
 db.session.add(user1)
 sb.session,commit()
 ________________________
 #see database value
 
 users = User.query.all()
 users
 
 ______________________
 all of code in terminal 
 
"""

# ______________________________________________________


if __name__ == "__main__":
    app.run(debug=True)
