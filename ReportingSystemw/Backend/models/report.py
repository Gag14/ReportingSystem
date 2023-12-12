from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from . import db

class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creation_time = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Define a relationship with the User model
    user = db.relationship('User', backref=db.backref('reports', lazy=True))
    # issue_ids = db.Column('Issue', backref='reports', viewonly=True)
    # issues = db.relationship('Issue', backref='reports', lazy='dynamic')

    def __init__(self, created_by):
        self.created_by = created_by
        self.issues = []

    def to_dict(self):
        issues = json.dumps(issues)
        return {
            "id": self.id,
            "creation_time": self.creation_time.isoformat(),
            "created_by": self.created_by,
            "issues": issues
        }
