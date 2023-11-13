from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from base import db

class Issue(db.Model):
    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    related_partner_id = db.Column(db.Integer, db.ForeignKey('partners.id'), nullable=False)
    content = db.Column(db.String, nullable=False)
    state = db.Column(db.Boolean, default=False)  # Assuming False means not solved
    creation_time = db.Column(db.DateTime, default=datetime.utcnow)
    duration_time = db.Column(db.Interval)

    # Define relationships with the User and Partner models
    user = db.relationship('User', backref=db.backref('issues', lazy=True))
    partner = db.relationship('Partner', backref=db.backref('issues', lazy=True))

    def __init__(self, created_by, related_partner_id, content):
        self.created_by = created_by
        self.related_partner_id = related_partner_id
        self.content = content

    def get_duration_time(self):
        if self.state:
            return self.duration_time
        else:
            return datetime.utcnow() - self.creation_time

    def to_dict(self):
        return {
            "id": self.id,
            "created_by": self.created_by,
            "related_partner_id": self.related_partner_id,
            "content": self.content,
            "state": self.state,
            "creation_time": self.creation_time.isoformat(),
            "duration_time": str(self.get_duration_time()),
            # Add other fields as needed
        }
