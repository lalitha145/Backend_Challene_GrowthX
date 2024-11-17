def validate_user_registration(data):
    """Validate user registration input."""
    errors = []
    if not data.get("email"):
        errors.append("Email is required.")
    if not data.get("password"):
        errors.append("Password is required.")
    return errors

def validate_assignment(data):
    """Validate assignment input."""
    errors = []
    if not data.get("task"):
        errors.append("Task is required.")
    if not data.get("admin"):
        errors.append("Admin is required.")
    return errors
