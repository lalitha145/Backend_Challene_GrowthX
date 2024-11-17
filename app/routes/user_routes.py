from flask import Blueprint
from app.controllers.user_controller import register_user, login_user, upload_assignment
from app.middleware.auth_middleware import jwt_required

user_blueprint = Blueprint('user', __name__)

user_blueprint.route('/register', methods=['POST'])(register_user)
user_blueprint.route('/login', methods=['POST'])(login_user)
user_blueprint.route('/upload', methods=['POST'])(jwt_required(upload_assignment))
