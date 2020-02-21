

class FlaskConfig:
    PORT = 8090
    SERVER_NAME = "localhost:%d" % PORT

    # Update later by using a random number generator and moving
    SECRET_KEY = 's3RBxy2H2J'

    DEBUG = True

    # Database
    HOST = "172.17.0.2"
    SCHEMA = "python"
    USERNAME = "root"
    PASSWORD = "dpmo4"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(USERNAME, PASSWORD, HOST, SCHEMA)
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = True
