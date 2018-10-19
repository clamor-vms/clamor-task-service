from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from models import ma, Task
from .TaskStatusSchema import TaskStatusSchema

# Custom validator


def must_not_be_blank(data):
    if not data:
        raise ValidationError('Foreign key not provided.')


class TaskSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    task_group_id = fields.Integer()
    task_status = fields.Nested(
        TaskStatusSchema,
        must_not_be_blank
    )
