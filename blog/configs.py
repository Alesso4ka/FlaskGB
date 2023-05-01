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
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path
    FLASK_ADMIN_SWATCH = 'cosmo'


class TestingConfig(BaseConfig):
    TESTING = True
