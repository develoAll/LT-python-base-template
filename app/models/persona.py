from app import db
from sqlalchemy.sql import func


class Persona(db.Model):
    __tablename__ = "persona"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido_paterno = db.Column(db.String(100))
    apellido_materno = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    fecha_nacimiento = db.Column(db.DateTime)
    fecha_creacion = db.Column(db.DateTime, server_default=func.now())
