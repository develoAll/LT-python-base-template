from app import db

career_course_association = db.Table(
    'career_course',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('id_career', db.Integer, db.ForeignKey('db_unfv.career.id', ondelete='CASCADE')),
    db.Column('id_course', db.Integer, db.ForeignKey('db_unfv.course.id', ondelete='CASCADE')),
    db.Column('state', db.Boolean, nullable=True),
    schema='db_unfv'
)


class CareerCourse(db.Model):
    __tablename__ = "career_course"
    __table_args__ = {'extend_existing': True, 'schema': 'db_unfv'}

    id = db.Column(db.Integer, primary_key=True)
    id_career = db.Column(db.Integer, db.ForeignKey('db_unfv.career.id', ondelete='CASCADE'))
    id_course = db.Column(db.Integer, db.ForeignKey('db_unfv.course.id', ondelete='CASCADE'))
    state = db.Column(db.Boolean, nullable=False, default=True)
