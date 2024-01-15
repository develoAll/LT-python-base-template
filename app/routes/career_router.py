from flask import Blueprint, request, jsonify
from app.controller import career

api_career = Blueprint("career", __name__)


@api_career.route('/postCreateCareer', methods=["POST"])
def post_create_career():
    data = career.create_career_detail(request.json)
    return jsonify(data)
