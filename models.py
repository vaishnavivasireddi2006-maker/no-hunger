from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'donor', 'ngo', 'volunteer', 'admin'
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    donations = db.relationship('Donation', backref='donor', lazy=True, cascade="all, delete-orphan")
    requests = db.relationship('PickupRequest', backref='ngo', lazy=True, cascade="all, delete-orphan")
    assignments = db.relationship('VolunteerAssignment', backref='volunteer', lazy=True, cascade="all, delete-orphan")
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Donation(db.Model):
    __tablename__ = 'donations'
    
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    food_item = db.Column(db.String(100), nullable=False)
    food_type = db.Column(db.String(50), nullable=False)  # 'Cooked Meal', 'Groceries', 'Bakery', 'Fruits & Veg'
    quantity = db.Column(db.String(50), nullable=False)
    location = db.Column(db.Text, nullable=False)
    expiry_time = db.Column(db.DateTime, nullable=False)
    image_path = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(20), default='available', nullable=False)  # 'available', 'requested', 'assigned', 'completed', 'cancelled'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    pickup_requests = db.relationship('PickupRequest', backref='donation', lazy=True, cascade="all, delete-orphan")
    volunteer_assignments = db.relationship('VolunteerAssignment', backref='donation', lazy=True, cascade="all, delete-orphan")

class PickupRequest(db.Model):
    __tablename__ = 'pickup_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    donation_id = db.Column(db.Integer, db.ForeignKey('donations.id', ondelete='CASCADE'), nullable=False)
    ngo_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.String(20), default='pending', nullable=False)  # 'pending', 'accepted', 'completed', 'cancelled'
    request_notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    volunteer_assignments = db.relationship('VolunteerAssignment', backref='pickup_request', lazy=True, cascade="all, delete-orphan")

class VolunteerAssignment(db.Model):
    __tablename__ = 'volunteer_assignments'
    
    id = db.Column(db.Integer, primary_key=True)
    donation_id = db.Column(db.Integer, db.ForeignKey('donations.id', ondelete='CASCADE'), nullable=False)
    pickup_request_id = db.Column(db.Integer, db.ForeignKey('pickup_requests.id', ondelete='CASCADE'), nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.String(20), default='assigned', nullable=False)  # 'assigned', 'picked_up', 'delivered', 'cancelled'
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    delivered_at = db.Column(db.DateTime, nullable=True)
