import os

class Config(object):
    SECRET_KEY = os.urandom(32)
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'postgresql://lecarabinuser:0000@localhost/lecarabin'
    SQLAlCHEMY_TRACK_MODIFICATIONS = False

class devConfig(Config):
    DEBUG = True
    FLASK_ADMIN_SWATCH = 'cerulean'
