import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')

def get_db_url(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'root'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    NAME = dbinfo.get('NAME') or 'test'

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "12334dasfsgfdsgwrghkkgdfhj4occvxKJDKJADMNNB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class PostgreSQLConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'postgresql',
        'DRIVER': 'psycopg2',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'main'
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

class MySQLConfig(Config):
    TESTING = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123321',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'test'
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

class SQLiteConfig(Config):

    DATABASE = {
        'ENGINE': 'sqlite',
        'DRIVER': 'psycopg2',
        'USER': 'postgres',
        'PASSWORD': '123321',
        'HOST': '123.56.13.139',
        'PORT': '5432',
        'NAME': 'main'
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

class StagingConfig(Config):

    DATABASE = {
        'ENGINE': 'postgresql',
        'DRIVER': 'psycopg2',
        'USER': 'postgres',
        'PASSWORD': '123321',
        'HOST': '123.56.13.139',
        'PORT': '5432',
        'NAME': 'testdb'
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

class ProductConfig(Config):

    DATABASE = {
        'ENGINE': 'postgresql',
        'DRIVER': 'psycopg2',
        'USER': 'postgres',
        'PASSWORD': '123321',
        'HOST': '123.56.13.139',
        'PORT': '5432',
        'NAME': 'testdb'
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

envs = {
    'postgreConfig': PostgreSQLConfig,
    'mysqlConfig': MySQLConfig,
    'staging': StagingConfig,
    'product': ProductConfig
}