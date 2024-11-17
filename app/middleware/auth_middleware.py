from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

def jwt_required(fn):
    """Custom middleware to enforce authentication."""
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            user = get_jwt_identity()
            if not user:
                return jsonify({"error": "Authentication required"}), 401
            request.user = user  # Attach user info to the request
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401
    return wrapper
