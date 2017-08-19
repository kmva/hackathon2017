from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(40))
    phonenumber = db.Column(db.Integer(20))

    def __init__(self, firstname, email, phonenumber, password):
        self.firstname = firstname.title()
        self.email = email.lower()
        self.phonenumber = phonenumber
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

class Dishes(db.Model):
    __tablename__ = 'dishes'
    uid = db.Column = db.Column(db.Integer, primary_key = True)
    dish_name = db.Column(db.String(100))
    price = db.Column(db.Integer(6))

    def __init__(self, dish_name, price):
        self.dish_name = dish_name.lower()
        self.price = price

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    uid = db.Column = db.Column(db.Integer, primary_key = True)
    restaurant_name = db.Column(db.String(100))
    email = db.Column(db.Integer(6))

    def __init__(self, restaurant_name, email):
        self.restaurant_name = restaurant_name.lower()
        self.email = email.lower()