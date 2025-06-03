# This file is used to create our db structure with the Flask-SQLAlchemy ORM.

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    linked_id = db.Column(db.Integer, nullable=True)
    link_precedence = db.Column(db.String, default='primary')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    deleted_at = db.Column(db.DateTime, nullable=True)
