import os


class Config:
    """
    This class represents the flask configuration
    """
    is_prod_environment = os.getenv('FLASK_ENV') == "production"

    if is_prod_environment:
        __username = os.getenv('DB_USER', 'sqlalchemy')
        __password = os.getenv('DB_PASSWORD', 'sqlalchemy')
        __host = os.getenv('DB_HOST', 'localhost')
        __port = os.getenv('DB_PORT', '5432')
        __db_name = os.getenv('DB_NAME', 'catalog')
        SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{__username}:{__password}@{__host}:{__port}/{__db_name}'
    else:
        import tempfile
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = f'sqlite:///catalogtest.db'
    APP_PORT = os.getenv('APP_PORT', "9001")
    APP_HOST = os.getenv('APP_HOST', "0.0.0.0")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
