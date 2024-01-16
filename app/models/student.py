from app import db
from sqlalchemy.sql import func


class Student(db.Model):
    __tablename__ = "student"
    __table_args__ = {'extend_existing': True, 'schema': 'db_unfv'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    mother_last_name = db.Column(db.String(100))
    father_last_name = db.Column(db.String(100))
    nick_name = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    codigo = db.Column(db.String(10))
    birthdate = db.Column(db.Date)
    photo = db.Column(db.String(500))
    sex = db.Column(db.String(10))
    mail = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=func.now())
    id_career = db.Column(db.Integer, db.ForeignKey('career.id'))
    # career = db.relationship('Career', backref='student')
