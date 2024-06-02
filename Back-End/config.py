import os

class Config:
    # set SECRET_KEY=0715
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://poshan:0715@localhost/personal_notes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_HTTPONLY = True  # Ensure the session cookie is HTTP only
    SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
