# Backend/config.py
import os
import secrets

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = secrets.token_hex(16)  # Generate a random 32-character hexadecimal string
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../../Database/newdb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST_URL = 'http://localhost:5000'  

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SECRET_KEY = secrets.token_hex(16)  # Generate a random 32-character hexadecimal string
    HOST_URL = 'https://your-production-url.com'  

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

print(Config.SQLALCHEMY_DATABASE_URI)