from app import db
from app.models.career_course import career_course_association

# career_course_association = db.Table(
#     'career_course',
#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('id_career', db.Integer, db.ForeignKey('career.id', ondelete='CASCADE')),
#     db.Column('id_course', db.Integer, db.ForeignKey('course.id', ondelete='CASCADE')),
#     db.Column('state', db.Boolean, nullable=True),
#     schema='db_unfv'
# )


class Career(db.Model):
    __tablename__ = "career"
    __table_args__ = {'extend_existing': True, 'schema': 'db_unfv'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(500), nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    courses = db.relationship('Course', secondary=career_course_association, backref='career')