import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'averysecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db:3306/survey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-User settings
    USER_ENABLE_EMAIL = False        # Enable email authentication
    USER_ENABLE_USERNAME = True    # Disable username authentication
    USER_UNAUTHENTICATED_ENDPOINT = 'login'

    LANGUAGES = ['en', 'es']
