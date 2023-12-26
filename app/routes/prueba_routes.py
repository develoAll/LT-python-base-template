from flask import Blueprint
from flask import jsonify
from app.models.persona import Persona

api_prueba = Blueprint("prueba", __name__)


@api_prueba.route('/texto')
def get_text_prueba():
    person = Persona.query.all()
    nombre = person[1].nombre
    return jsonify({'nombre': nombre})
