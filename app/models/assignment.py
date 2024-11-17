from flask import current_app
from app import mongo

class Assignment:
    @staticmethod
    def create_assignment(data):
        assignments = mongo.db.assignments
        assignment_id = assignments.insert_one(data).inserted_id
        return str(assignment_id)

    @staticmethod
    def find_by_admin(admin_id):
        return list(mongo.db.assignments.find({"adminId": admin_id}))
