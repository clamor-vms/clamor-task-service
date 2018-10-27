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
from services import TaskService
# from models import db, TaskGroup, Task, TaskStatus
# from schemas import TaskSchema

# tasks_schema = TaskSchema(many=True)
# task_schema = TaskSchema()

taskService = TaskService()


class TaskController(Resource):
    def get(self):
        # get :id
        if request.args:
            param = request.args['id']
            if param:
                result = taskService.GetTask(param)
                return {
                    'status': 'success',
                    'data': result
                }, 200
            else:
                return {
                    'status': 'not found',
                    'message': 'couldn\'t find any records'
                }, 404
        else:
            result = taskService.GetTasks()
            return {"status": "succcess", "data": result}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input provided."}, 400

        result, err = taskService.CreateTask(json_data)

        if err:
            return {'status': 'error', 'info': err}, 400

        return {'status': 'success', 'data': result}, 201

    # def put(self):
    #     json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {"message": "No input provided."}, 400
    #     data, errors = task_schema.load(json_data)
    #     if errors:
    #         return {"status": "error", "data": data}

    #     task = Task.query.filter_by(
    #         task_group_id=data["task_group_id"],
    #         id=data["id"]
    #     ).first()
    #     if not task:
    #         return {"error": "Something went wrong getting task."}

    #     task.name = data['name']
    #     task.description = data['description']
    #     db.session.commit()

    #     result = task_schema.dump(task).data

    #     return {"status": 'success', 'data': result}, 204

    # def delete(self):
    #     json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    #     # Validate and deserialize input
    #     data, errors = task_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #     task = Task.query.filter_by(
    #         task_group_id=data["task_group_id"],
    #         id=data["id"]
    #     ).delete()

    #     db.session.commit()
    #     result = task_schema.dump(task).data

    #     return {
    #         "status": 'success',
    #         'retrieved data for delete(delete not set)': result
    #     }, 204
