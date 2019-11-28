class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    DB_SERVER = '127.0.0.1'
    DIALECT = 'mysql'               # 数据库类型
    DRIVER = 'pymysql'              # 连接数据库驱动
    USERNAME = 'root'               # 用户名
    PASSWORD = '980612ssj@%'        # 密码
    HOST = '101.132.70.184'         # 服务器
    PORT = '3306'                   # 端口
    DATABASE = 'JiaBlog'            # 数据库名
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,PORT, DATABASE)
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:980612ssj@%@101.132.70.184:3306/JiaBlog"
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