import os


class Config:
    """ Parent configuration class """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True
    TESTING = False
    DATABASE_URL = os.getenv('postgresql://localhost/politico')


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database"""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv('TEST_DATABASE_URL')

app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig
}