from flask import Blueprint
from app.models import persona

api_prueba = Blueprint("prueba", __name__)


@api_prueba.route('/texto')
def get_text_prueba():
    person = persona.query.all()
    return person
