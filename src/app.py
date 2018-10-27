'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from flask import Blueprint
from flask_restful import Api
from controllers import TaskGroupController, TaskController, TaskStatusController, TaskAssignmentController

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Route
api.add_resource(TaskGroupController, '/taskGroups')
api.add_resource(TaskController, '/tasks')
api.add_resource(TaskStatusController, '/statuses')
api.add_resource(TaskAssignmentController, '/assignments')
