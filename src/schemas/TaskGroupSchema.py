from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, post_load
from models import ma, TaskGroup
from schemas import TaskSchema


class TaskGroupSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    tasks = fields.List(fields.Nested(TaskSchema))
