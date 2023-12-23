from flask import Blueprint, render_template
from config import Config

home = Blueprint('home', __name__, template_folder=Config.TEMPLATE_FOLDER)


# Ruta inicial
@home.route('/')
@home.route('/home')
def index():
    return render_template('index.html')
