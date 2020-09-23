from app import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r %r' % (self.name, self.email)

class Scan(db.Model): 
    __tablename__ = "Scan"
    id = db.Column(db.Integer, primary_key=True)
    check_in_time = db.Column(db.Datetime)
    mask_detected = db.Column(db.Boolean, default=False)
    temperature = db.Column(db.Double,nullable=False)
    
    def __init__(self, check_in_time, mask_detected, temperature):
        self.check_in_time = datetime.now()
        self.mask_detected = mask_detected
        self.temperature = temperature

    def __repr__(self):
        return '<Scan %r %r %r' % (self.check_in_time, self.mask_detected, self.temperature)

    