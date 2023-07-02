import os
import secrets
# TODO: Should be env variables
UPLOAD_IMAGE_PATH: str = "./lc_contents/images"


class Config(object):
    """ Defines the Configuration class file"""

    SECRET_KEY = secrets.token_hex(32)

    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'postgresql://lecarabinuser:0000@localhost/lecarabin'

    SQLAlCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = UPLOAD_IMAGE_PATH


class DevConfig(Config):
    """ Defines the developpement configuration object"""

    DEBUG = True

