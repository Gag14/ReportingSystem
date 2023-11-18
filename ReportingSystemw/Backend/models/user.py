from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _first_name = db.Column(db.String(50), nullable=False)
    _last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(5), default="en")
    state = db.Column(db.Integer, default=1)  # 1 for active, 0 for inactive
    role = db.Column(db.String(20), nullable=False)
    points = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, first_name, last_name, email, role, username, password):
        self._first_name = first_name
        self._last_name = last_name
        self.email = email
        self.role = role
        self.username = username
        self.set_password(password)

    def set_first_name(self, first_name):
        if first_name.isalpha():
            self._first_name = first_name
        else:
            raise ValueError("Invalid first name. Only letters are allowed.")

    def set_last_name(self, last_name):
        if last_name.isalpha():
            self._last_name = last_name
        else:
            raise ValueError("Invalid last name. Only letters are allowed.")

    def set_email(self, email):
        # Add email validation logic if needed
        self.email = email

    def set_username(self, username):
        # Add username validation logic if needed
        self.username = username

    def set_password(self, password):
        if len(password) >= 6:
            self.password_hash = generate_password_hash(password)
        else:
            raise ValueError("Password must be at least 6 characters.")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "email": self.email,
            "language": self.language,
            "state": "Active" if self.state == 1 else "Inactive",
            "role": self.role,
            "points": self.points,
            "username": self.username,
        }
