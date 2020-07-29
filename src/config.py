import os


class Development(object):
    """Dev config"""

    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv(str(os.urandom(30)))
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")


class Production(object):
    """Production config"""

    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv(str(os.urandom(30)))
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")


app_config = {
    "development": Development,
    "production": Production,
}
