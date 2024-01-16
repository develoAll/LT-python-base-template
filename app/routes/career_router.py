from flask import Blueprint, request, jsonify
from app.controller import career

api_career = Blueprint("career", __name__)


@api_career.route('/postCreateCareer', methods=["POST"])
def post_create_career():
    data = career.create_career_detail(request.json)
    return jsonify(data)


@api_career.route('/getCardCareer', methods=["GET"])
def get_card_career():
    data = career.get_all_carrer_card()
    return jsonify(data)


@api_career.route('/getIdNameCareer', methods=["GET"])
def get_id_name_career():
    data = career.get_all_id_name_carrer()
    return jsonify(data)
