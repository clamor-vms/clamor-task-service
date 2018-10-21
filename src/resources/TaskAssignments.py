from flask import request
from flask_restful import Resource
from models import db, TaskAssignment, Task
from schemas import TaskAssignmentSchema

task_assignments_schema = TaskAssignmentSchema(many=True)
task_assignment_schema = TaskAssignmentSchema()


class TaskAssignmentResource(Resource):
    def get(self):
        # get :id
        if request.args:
            param = request.args['id']
            if param:
                taskAssignment = TaskAssignment.query.filter_by(
                    id=param).first()
                result = task_assignment_schema.dump(taskAssignment).data
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
            allAssignments = TaskAssignment.query.all()
            assignmentData = task_assignments_schema.dump(allAssignments).data
            return {"status": "succcess", "data": assignmentData}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = task_assignment_schema.load(json_data)
        if errors:
            return {
                'err': errors,
                'msg': 'Validation error',
                'tried': json_data
            }, 422

        print("task_id: ", data['task_id'])

        task = Task.query.filter_by(
            id=data['task_id']
        ).first()

        if not task:
            return {'message': 'Task does not exist.'}, 400

        taskAssignment = TaskAssignment(
            task_id=json_data['task_id'],
            user_id=json_data['user_id']
        )

        db.session.add(taskAssignment)
        db.session.commit()

        result = task_assignment_schema.dump(taskAssignment).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = task_assignment_schema.load(json_data)
        if errors:
            return errors, 422
        taskAssignment = TaskAssignment.query.filter_by(
            id=data['id']).first()
        if not taskAssignment:
            return {'message': 'Task assignment does not exist'}, 400

        taskAssignment.user_id = data['user_id']
        taskAssignment.task_id = data['task_id']
        db.session.commit()

        result = task_assignment_schema.dump(taskAssignment).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = task_assignment_schema.load(json_data)
        if errors:
            return errors, 422
        taskGroup = TaskAssignment.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = task_assignment_schema.dump(taskGroup).data

        return {"status": 'success', 'data': result}, 204
