import os
from secrets import token_hex
from datetime import timedelta

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../newdb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST_URL = 'http://localhost:5000'  
    JWT_SECRET_KEY = token_hex(16)  # Set your JWT secret key

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SECRET_KEY = token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../newdb.db'  # Modify this for your production database
    HOST_URL = 'http://localhost:5000'  

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
