from app import db
from sqlalchemy.sql import func


class Persona(db.Model):
    __tablename__ = "persona"
    __table_args__ = {'extend_existing': True, 'schema': 'db_unfv'}

    idpersona = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido_paterno = db.Column(db.String(50))
    apellido_materno = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    fecha_nacimiento = db.Column(db.DateTime)
    fecha_creacion = db.Column(db.DateTime, default=func.now())
