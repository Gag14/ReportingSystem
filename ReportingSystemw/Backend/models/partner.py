from flask_sqlalchemy import SQLAlchemy

from . import db


class Partner(db.Model):
    __tablename__ = 'partners'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=True)

    def __init__(self, name, priority=None):
        self.name = name
        self.priority = priority

    def get_active_issues(self):
        # Assuming issues have a boolean field 'state' indicating if they are solved or not
        return [issue for issue in self.issues if not issue.state]

    def get_done_issues(self):
        # Assuming issues have a boolean field 'state' indicating if they are solved or not
        return [issue for issue in self.issues if issue.state]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "priority": self.priority,
            # Add other fields as needed
        }
