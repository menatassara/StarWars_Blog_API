from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(250), nullable=False)
    starships = db.Column(db.String(250), nullable=False)
    vehicles = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)

        def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach


