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

from flask import request
from flask_restful import Resource
from models import db, TaskStatus
from schemas import TaskStatusSchema
from flask_jwt_simple import jwt_required

task_statuses_schema = TaskStatusSchema(many=True)
task_status_schema = TaskStatusSchema()


class TaskStatusController(Resource):
    @jwt_required
    def get(self):
        task_statuses = TaskStatus.query.all()
        result = task_statuses_schema.dump(task_statuses).data
        return {"status": "succcess", "data": result}, 200
