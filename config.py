# desde aqui se deberia realizar las configuraciones del servidor
from dotenv import load_dotenv  # Instalar con pip install python-dotenv

load_dotenv()  # Carga todo el contenido de .env en variables de entorno


class Config:
    SERVER_NAME = "localhost:7001"
    DEBUG = True

    TEMPLATE_FOLDER = "templates/"
