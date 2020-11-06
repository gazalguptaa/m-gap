from app import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.String(255), nullable=False)
    register_image = db.Column(db.LargeBinary)
    
    def __init__(self, name, email, gender, age, contact, register_image):
        self.name = name
        self.email = email
        self.gender = gender
        self.age = age
        self.contact = contact
        self.register_image = register_image

    def __repr__(self):
        return '<User %r %r %r %r %r' % (self.name, self.email, self.gender, self.age, self.contact, self.register_image)

class Scan(db.Model): 
    __tablename__ = "Scan"
    id = db.Column(db.Integer, primary_key=True)
    check_in_time = db.Column(db.DateTime)
    mask_detected = db.Column(db.Boolean, default=False)
    temperature = db.Column(db.Float,nullable=False)
    verify_image = db.Column(db.LargeBinary)
    
    def __init__(self, check_in_time, mask_detected, temperature, verify_image):
        self.check_in_time = datetime.now()
        self.mask_detected = mask_detected
        self.temperature = temperature
        self.verify_image = verify_image

    def __repr__(self):
        return '<Scan %r %r %r %r' % (self.check_in_time, self.mask_detected, self.temperature, self.verify_image)

    