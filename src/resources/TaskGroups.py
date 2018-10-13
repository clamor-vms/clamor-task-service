from flask import request
from flask_restful import Resource
from models.TaskGroup import TaskGroupSchema, TaskGroup

taskgroups_schema = TaskGroupSchema(many=True)
taskgroup_schema = TaskGroupSchema()


class TaskGroupResource(Resource):
    def get(self):
        taskgroups = TaskGroup.query.all()
        taskgroups = taskgroups_schema.dump(taskgroups).data
        return {'status': 'success', 'data': taskgroups}, 200
