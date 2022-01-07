from flask import Flask
from config import Config
from extensions import db
from flask_migrate import Migrate
from flask_restful import Api

from resources.catalogbrand import (
    CatalogBrandListResource,
    CatalogBrandResource,
)
from resources.catalogtype import (
    CatalogTypeListResource,
    CatalogTypeResource
)

from resources.catalogitem import (
    CatalogItemListResource,
    CatalogItemResource
)


def create_app() -> Flask:
    """
    Create the flask application Object
    :return: Flask Application Object
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    """
    Perform database initialization and migrate the database and register other extensions
    :param app:
    :return:
    """
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    """
    This method is used to register the app resources
    :param app: flask app
    :return:
    """
    api = Api(app)
    api.add_resource(CatalogBrandListResource, '/api/v1/catalog/brands')
    api.add_resource(CatalogTypeListResource, '/api/v1/catalog/types')
    api.add_resource(CatalogBrandResource, '/api/v1/catalog/brands/<int:id>')
    api.add_resource(CatalogTypeResource, '/api/v1/catalog/types/<int:id>')
    api.add_resource(CatalogItemListResource, '/api/v1/catalog/items')
    api.add_resource(CatalogItemResource, '/api/v1/catalog/items/<int:id>')


if __name__ == '__main__':
    catalog_app = create_app()

    catalog_app.run(port=Config.APP_PORT, host=Config.APP_HOST, debug=True)
