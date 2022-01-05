from flask import Flask
from config import Config
from extensions import db
from flask_migrate import  Migrate


def create_app() -> Flask:
    """
    Create the flask application Object
    :return: Flask Application Object
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    return app

def register_extensions(app):
    """
    Perform database initialization and migrate the database and register other extensions
    :param app:
    :return:
    """
    db.init_app(app)
    migrate = Migrate(app, db)


if __name__ == '__main__':
    catalog_app = create_app()

    catalog_app.run(port=Config.APP_PORT, host=Config.APP_HOST, debug=True)
