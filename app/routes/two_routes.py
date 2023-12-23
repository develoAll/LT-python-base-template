from flask import Blueprint


api_two = Blueprint("two", __name__)


@api_two.route('/texto')
def get_text_prueba():
    return '<h1>Hola mundo - prueba2h1>'
