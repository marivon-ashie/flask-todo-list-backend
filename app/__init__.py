from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from flask_login import LoginManager

db =SQLAlchemy()
login_manager=LoginManager()

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = str(uuid4())
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"



    from  app.auth.routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from app.task.routes import task as task_blueprint
    app.register_blueprint(task_blueprint)
    
    with app.app_context():
        from .import models
        db.create_all()
    return app 
@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))