import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"
    WTF_CSRF_ENABLED = True


class DevConfig(BaseConfig):
    file_path = os.path.abspath(os.getcwd()) + "/blog.db"
    # file_path = "D:/FlaskGB/blog.db"

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path
    FLASK_ADMIN_SWATCH = 'cosmo'
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class TestingConfig(BaseConfig):
    TESTING = True
