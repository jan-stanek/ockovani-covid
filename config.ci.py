class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SEND_FILE_MAX_AGE_DEFAULT = 300

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class myConfig:
    FLASK_APP = 'app.py'
    FLASK_DEBUG = 1
    SQLALCHEMY_DATABASE_URI = 'postgresql://__DB_USER__:__DB_PASSWORD__@__DB_HOST__:__DB_PORT__/__DB_NAME__'
