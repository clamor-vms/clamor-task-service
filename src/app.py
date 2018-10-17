from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.TaskGroups import TaskGroupResource
from resources.Tasks import TaskResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Route
api.add_resource(Hello, '/Hello')
api.add_resource(TaskGroupResource, '/taskGroups')
api.add_resource(TaskResource, '/tasks')
