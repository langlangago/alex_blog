from flask import Flask
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager
from config import Config

bootstrap = Bootstrap()
admin = Admin(name='Blog', template_mode='bootstrap3')
db = SQLAlchemy()
moment = Moment()
login = LoginManager()

# from app.models import User, Post


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Config.init_app(app)

    bootstrap.init_app(app)
    admin.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    login.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

