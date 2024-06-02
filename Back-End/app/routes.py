from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, Note, Category

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid data'}), 400
    
    username = data['username']
    email = data['email']
    password = data['password']
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid data'}), 400

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 400

    login_user(user)
    return jsonify({'message': 'Login successful'}), 200

@main.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

@main.route('/notes', methods=['GET', 'POST'])
@login_required
def manage_notes():
    if request.method == 'POST':
        data = request.json
        if not data or 'title' not in data or 'description' not in data or 'category' not in data:
            return jsonify({'message': 'Invalid data'}), 400

        note = Note(title=data['title'], description=data['description'], category=data['category'], author=current_user)
        db.session.add(note)
        db.session.commit()
        return jsonify({'message': 'Note added successfully'}), 201

    notes = current_user.notes.all()
    return jsonify([{'id': note.id, 'title': note.title, 'description': note.description, 'category': note.category, 'timestamp': note.timestamp} for note in notes]), 200

@main.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{'id': category.id, 'name': category.name} for category in categories]), 200

@main.route('/user', methods=['GET'])
@login_required
def get_user():
    return jsonify({'username': current_user.username, 'email': current_user.email}), 200
