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
from models import db, TaskGroup
from schemas.TaskGroupSchema import TaskGroupSchema

taskgroups_schema = TaskGroupSchema(many=True)
taskgroup_schema = TaskGroupSchema()


class TaskGroupResource(Resource):
    def get(self):
        # get :id
        if request.args:
            param = request.args['id']
            if param:
                taskGroup = TaskGroup.query.filter_by(id=param).first()
                result = taskgroup_schema.dump(taskGroup).data
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
            # get all
            taskgroups = TaskGroup.query.all()
            taskgroups = taskgroups_schema.dump(taskgroups).data
            return {'status': 'success', 'data': taskgroups}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = taskgroup_schema.load(json_data)
        if errors:
            return {
                'err': errors,
                'msg': 'Validation error',
                'tried': json_data
            }, 422
        taskGroup = TaskGroup.query.filter_by(name=data['name']).first()
        if taskGroup:
            return {'message': 'Task Group already exists'}, 400
        taskGroup = TaskGroup(
            name=json_data['name'],
            description=json_data['description']
        )

        db.session.add(taskGroup)
        db.session.commit()

        result = taskgroup_schema.dump(taskGroup).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = taskgroup_schema.load(json_data)
        if errors:
            return errors, 422
        taskGroup = TaskGroup.query.filter_by(id=data['id']).first()
        if not taskGroup:
            return {'message': 'Task Group does not exist'}, 400
        taskGroup.name = data['name']
        taskGroup.description = data['description']
        db.session.commit()

        result = taskgroup_schema.dump(taskGroup).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = taskgroup_schema.load(json_data)
        if errors:
            return errors, 422
        taskGroup = TaskGroup.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = taskgroup_schema.dump(taskGroup).data

        return {"status": 'success', 'data': result}, 204
