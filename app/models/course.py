from app import db
from app.models.career_course import career_course_association


class Course(db.Model):
    __tablename__ = "course"
    __table_args__ = {'extend_existing': True, 'schema': 'db_unfv'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    image = db.Column(db.String(500))
    careers = db.relationship('Career', secondary=career_course_association, backref='course')
