from flask import Blueprint, request, jsonify
from app.controller import student

api_student = Blueprint("student", __name__)


@api_student.route('/getByCourse')
def get_students_by_course():
    data = student.get_by_course()
    return jsonify(data)


@api_student.route('/postCreateStudent', methods=["POST"])
def post_create_student():
    data = student.create_student(request.json)
    return jsonify(data)
