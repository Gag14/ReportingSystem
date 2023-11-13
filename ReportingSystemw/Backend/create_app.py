# # # from flask import Flask, render_template
# # # from flask_sqlalchemy import SQLAlchemy
# # # from config import Config
# # # from Backend.models.base import db
# # # from Backend.models import user, partner, issue, report
# # # app = Flask(__name__)
# # # app.config['DEBUG'] = Config.DEBUG
# # # app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

# # # db.init_app(app)

# # # with app.app_context():
# # #     from Backend.models import user, partner, issue, report

# # #     db.create_all()
# # #     print("Database created successfully!")

# # # app.run()

# # from flask import Flask
# # from models.base import db
# # from sqlalchemy import create_engine

# # app = Flask(__name__)
# # # Load configuration from a separate file
# # app.config.from_pyfile('config.py')
# # # Connect to the database using SQLAlchemy's create_engine
# # engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# # # Bind the engine to the Base class
# # db.metadata.bind = engine
# # # Create tables based on the defined models
# # with app.app_context():
# #     db.metadata.create_all()

# # app.run()
# from flask import Flask
# from models.base import db
# from models import create_app  # Import the create_app function

# app, db = create_app()

# # Create tables based on the defined models
# with app.app_context():
#     db.create_all()

# app.run()
# create_app.py
from flask import Flask
from models.base import db  # Assuming you have a 'base.py' file in the 'models' package

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    return app, db

app, db = create_app()

# Create tables based on the defined models
with app.app_context():
    db.create_all()

app.run()
