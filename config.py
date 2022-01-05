import os


class Config:
    """
    This class represents the flask configuration
    """
    __username = os.getenv('DB_USER', 'sqlalchemy')
    __password = os.getenv('DB_PASSWORD', 'sqlalchemy')
    __host = os.getenv('DB_HOST', 'localhost')
    __port = os.getenv('DB_PORT', '5432')
    __db_name = os.getenv('DB_NAME', 'catalog')

    DEBUG = True
    APP_PORT = os.getenv('APP_PORT', "9001")
    APP_HOST = os.getenv('APP_HOST', "0.0.0.0")
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{__username}:{__password}@{__host}:{__port}/{__db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
