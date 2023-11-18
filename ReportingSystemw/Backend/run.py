from flask import Flask, request, jsonify
from flask import render_template
from flask import current_app

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import jwt
import datetime
from flask_jwt_extended import get_jwt

from config import Config
from models import create_app, db
from models.user import User
from models.report import Report
from models.issue import Issue
from models.partner import Partner
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from datetime import timedelta


app = create_app('production')
CORS(app)
jwt = JWTManager(app)
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

def generate_jwt_token(user):
    # 'identity' is a special field in JWT that is used to store the identity of the user
    identity = {'id': user.id, 'username': user.username}
    
    # You can customize the expiration time based on your needs
    expires = timedelta(days=1)  # 1 day in this example
    
    # Create the JWT token
    token = create_access_token(identity=identity, expires_delta=expires)
    return token
# @app.route('/')
# # def index():
# #     # Example route
# #     return 'Hello, Support Reporting System!'
# # app = Flask(__name__)

# Assuming you have already initialized the database (db) and created tables
# @app.route('/')
# def page():
#     return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    # Retrieve the user from the database based on the provided username
    user = authenticate(data['username'], data['password'])

    if user and user.check_password(data['password']):
        # Generate JWT token
        token = generate_jwt_token(user)
        user_data = user.to_dict()
        return jsonify({'message': 'Login successful', 'user': user_data, 'token': token})
    else:
        # Return an error message for failed login
        return jsonify({'error': 'Invalid username or password'}), 401
    



@app.route('/register', methods=['POST'])
def register():
    data = request.json  # Assuming the client sends JSON data with registration information

    # Check if all required fields are present
    required_fields = ['first_name', 'last_name', 'email', 'role', 'username', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if the username is already taken
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already taken'}), 400

    # Create a new user
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        role=data['role'],
        username=data['username'],
        password=data['password']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registration successful', 'user': new_user.to_dict()}), 201


blacklist = set()
# Check if a token is blacklisted before processing a protected endpoint
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    # Your logic here to check if the token is in the blacklist
    return jti in blacklist

# Logout endpoint
@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    blacklist.add(jti)
    return jsonify({'message': 'Successfully logged out'}), 200


# Handle expired tokens
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({'message': 'Token has expired'}), 401


@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    current_user = get_jwt_identity()

    # Retrieve all users from the database
    users = User.query.all()

    # Convert the list of users to a JSON format
    users_list = [user.to_dict() for user in users]

    # Return the JSON response
    return jsonify({'users': users_list})





@app.route('/addpartner', methods=['POST'])
@jwt_required()
def create_partner():
    # Get data from the request
    data = request.get_json()
    current_user = get_jwt_identity()

    # Extract relevant information from the data
    name = data.get('name')
    priority = data.get('priority')
    # Add other fields as needed

    # Perform any necessary validation on the data

    # Create a new partner instance
    new_partner = Partner(name=name, priority=priority)
    # Add other fields as needed

    # Save the partner to the database
    db.session.add(new_partner)
    db.session.commit()

    # Return a JSON response indicating success
    return jsonify({'message': 'Partner created successfully', 'partner_id': new_partner.id}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)