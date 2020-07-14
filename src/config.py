import os


class Development(object):
    """Dev config"""
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv(str(os.urandom(30)))


class Production(object):
    """Production config"""
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv(str(os.urandom(30)))


app_config = {
    'development': Development,
    'production': Production,
}
