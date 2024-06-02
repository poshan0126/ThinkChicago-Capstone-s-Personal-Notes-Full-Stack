from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'main.login'

    CORS(app, supports_credentials=True, origins=['http://localhost:3001']) # Enable CORS with credentials

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
