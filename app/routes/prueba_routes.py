from flask import Blueprint


api_prueba = Blueprint("prueba", __name__)


@api_prueba.route('/texto')
def get_text_prueba():
    return '<h1>Hola mundo - prueba<h1>'
