from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    # Import and register blueprints
    from app.routes.user_routes import user_blueprint
    from app.routes.admin_routes import admin_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(admin_blueprint, url_prefix='/admins')
    
    return app
