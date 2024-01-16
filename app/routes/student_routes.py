from flask import Blueprint, request, jsonify
from app.controller import student

api_student = Blueprint("student", __name__)


@api_student.route('/getAllStudent', methods=["GET"])
def get_all_students():
    data = student.get_all_stundent()
    return jsonify(data)


@api_student.route('/postCreateStudent', methods=["POST"])
def post_create_student():
    data = student.create_student(request.json)
    return jsonify(data)


@api_student.route('/postCreateEnrollCareer', methods=["POST"])
def post_enroll_career():
    data = student.enroll_career_student(request.json)
    return jsonify(data)
