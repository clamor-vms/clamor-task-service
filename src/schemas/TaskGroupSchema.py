from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, post_load
from models import ma, TaskGroup
from .TaskSchema import TaskSchema
# from models.TaskGroup import TaskGroup


class TaskGroupSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    tasks = fields.List(fields.Nested(TaskSchema()))

    # @post_load
    # def create_task_group(self, data):
    #     return TaskGroup(data)
