
class Config(object):
    '''parent configuration file'''
    DEBUG = True
    SECRET_KEY = 'hardtoguess'
    ENV = 'development'
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    url = "dbname = 'stackoverflow_db' user = 'postgres' host = 'localhost' port = '5432'  password = 'admin'"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    url = "dbname = 'test_db' user = 'postgres' host = 'localhost' port = '5432' password = 'admin'"


class StaginConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StaginConfig,
    'production': ProductionConfig
}

db_url = DevelopmentConfig.url
test_url = TestingConfig.url
secret_key = Config.SECRET_KEY