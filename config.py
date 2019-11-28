class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    DB_SERVER = '127.0.0.1'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:980612ssj@%@101.132.70.184:3306/JiaBlog"
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    JSON_AS_ASCII = False
    SECRET_KEY = '123456'


class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = '118.25.79.249'


class DevelopmentConfig(Config):
    """Uses development database server."""
    DB_SERVER = 'localhost'
    DEBUG = True


class TestingConfig(Config):
    """Uses testing database server."""
    DB_SERVER = 'localhost'
    DEBUG = True