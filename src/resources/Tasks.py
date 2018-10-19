from flask import request
from flask_restful import Resource
from models import db, TaskGroup, Task
from schemas import TaskSchema

tasks_schema = TaskSchema(many=True)
task_schema = TaskSchema()


class TaskResource(Resource):
    def get(self):
        tasks = Task.query.all()
        tasks = tasks_schema.dump(tasks).data
        return {"status": "succcess", "data": tasks}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input provided."}, 400
        # validate / deserialize input.
        data, errors = task_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        task_group_id = TaskGroup.query.filter_by(
            id=data["task_group_id"]).first()
        if not task_group_id:
            return {"error": "Task group not found"}
        task = Task(
            task_group_id=data["task_group_id"],
            name=data["name"],
            description=data["description"]
        )
        db.session.add(task)
        db.session.commit()

        result = task_schema.dump(task).data

        return {"status": "success", "data": result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input provided."}, 400
        data, errors = task_schema.load(json_data)
        if errors:
            return {"status": "error", "data": data}

        task = Task.query.filter_by(
            task_group_id=data["task_group_id"],
            id=data["id"]
        ).first()
        if not task:
            return {"error": "Something went wrong getting task."}

        task.name = data['name']
        task.description = data['description']
        db.session.commit()

        result = task_schema.dump(task).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = task_schema.load(json_data)
        if errors:
            return errors, 422
        task = Task.query.filter_by(
            task_group_id=data["task_group_id"],
            id=data["id"]
        ).delete()

        db.session.commit()
        result = task_schema.dump(task).data

        return {
            "status": 'success',
            'retrieved data for delete(delete not set)': result
        }, 204
