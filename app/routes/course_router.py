from flask import Blueprint, jsonify
from app.controller import course

api_course = Blueprint("course", __name__)


@api_course.route('/getAllCourse')
def get_students_by_course():
    data = course.get_all_course()
    return jsonify(data)
