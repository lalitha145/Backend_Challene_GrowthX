from flask import Blueprint
from app.controllers.admin_controller import view_assignments, accept_assignment, reject_assignment
from app.middleware.auth_middleware import jwt_required

admin_blueprint = Blueprint('admin', __name__)

admin_blueprint.route('/assignments', methods=['GET'])(jwt_required(view_assignments))
admin_blueprint.route('/assignments/<string:assignment_id>/accept', methods=['POST'])(jwt_required(accept_assignment))
admin_blueprint.route('/assignments/<string:assignment_id>/reject', methods=['POST'])(jwt_required(reject_assignment))
