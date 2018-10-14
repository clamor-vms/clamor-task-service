from flask import request
from flask_restful import Resource
from models.Model import db
from models.TaskGroupSchema import TaskGroupSchema
from models.TaskGroup import TaskGroup

taskgroups_schema = TaskGroupSchema(many=True)
taskgroup_schema = TaskGroupSchema()


class TaskGroupResource(Resource):
    def get(self):
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
