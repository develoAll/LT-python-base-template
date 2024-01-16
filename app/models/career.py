from app import db
from app.models.career_course import career_course_association


class Career(db.Model):
    __tablename__ = "career"
    __table_args__ = {'extend_existing': True, 'schema': 'db_unfv'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.Text, nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    courses = db.relationship('Course', secondary=career_course_association, backref='career')
