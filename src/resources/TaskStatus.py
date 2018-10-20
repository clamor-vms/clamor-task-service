from flask import request
from flask_restful import Resource
from models import db, TaskStatus
from schemas import TaskStatusSchema

task_statuses_schema = TaskStatusSchema(many=True)
task_status_schema = TaskStatusSchema()


class TaskStatusResource(Resource):
    def get(self):
        task_statuses = TaskStatus.query.all()
        task_statuses = task_status_schema.dump(task_statuses).data
        return {"status": "succcess", "data": task_statuses}, 200