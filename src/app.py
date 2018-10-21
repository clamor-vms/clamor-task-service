from flask import Blueprint
from flask_restful import Api
from resources import TaskGroupResource, TaskResource, TaskStatusResource, TaskAssignmentResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Route
api.add_resource(TaskGroupResource, '/taskGroups')
api.add_resource(TaskResource, '/tasks')
api.add_resource(TaskStatusResource, '/status')
api.add_resource(TaskAssignmentResource, '/assignments')
