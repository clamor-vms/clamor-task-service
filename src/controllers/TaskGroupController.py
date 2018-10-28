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
from services import TaskGroupService
from flask_jwt_simple import jwt_required

groupService = TaskGroupService()


class TaskGroupController(Resource):
    @jwt_required
    def get(self):
        # get :id
        if request.args:
            param = request.args['id']
            if param:
                result = groupService.GetGroup(param)
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
            result = groupService.GetGroups()
            return {'status': 'success', 'data': result}, 200

    @jwt_required
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        result, err = groupService.CreateGroup(json_data)

        if err:
            return {'status': 'error', 'info': err}

        return {'status': 'success', 'data': result}, 201

    @jwt_required
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        result, err = groupService.UpdateGroup(json_data)

        if err:
            return {'status': 'error', 'info': err}
        return {'status': 'success', 'data': result}, 201

    @jwt_required
    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        result, err = groupService.DeleteGroup(json_data)

        if err:
            return {'status': 'error', 'info': err}
        return {'status': 'success', 'data': result}, 201
