# Indicamos que desde aqui correra nuestro programa
from app import create_app

if __name__ == "__main__":
    application = create_app()
    application.run()  # No añadir parámetros, modificar directamente en Config
