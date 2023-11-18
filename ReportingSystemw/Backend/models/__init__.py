from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import the CORS class
from config import app_config


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../Database.newdb.db'  # Use your actual database URI
    app.config.from_object(app_config[config_name])
    app.config['JWT_AUTH_URL_RULE'] = '/login'  # Define your login URL for JWT authentication
    CORS(app)

    db.init_app(app)

    return app
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt import JWT
# from config import app_config

# db = SQLAlchemy()

# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(app_config[config_name])
#     app.config['JWT_AUTH_URL_RULE'] = '/login'  # Define your login URL for JWT authentication

#     # Initialize extensions
#     db.init_app(app)
#     jwt = JWT(app, authenticate, identity)

#     # Import and register blueprints
#     from your_module.auth import auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     return app

# Replace 'your_module' with the actual module name where you have your blueprints.
# You need to define 'auth_blueprint' in your 'auth' module.
