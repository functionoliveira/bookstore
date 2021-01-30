import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'teste123'
    SQLALCHEMY_DATABASE_URI = 'postgres://root:teste123@bookstore-database/bookstore'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
