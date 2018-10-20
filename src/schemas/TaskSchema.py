from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, post_load
from models import ma
from schemas import TaskStatusSchema, TaskAssignmentSchema

# Custom validator


def must_not_be_blank(data):
    if not data:
        raise ValidationError('Foreign key not provided.')


class TaskSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    task_group_id = fields.Integer()
    task_status_id = fields.Integer()
    assignments = fields.List(fields.Nested(TaskAssignmentSchema))
#   task_status_id = fields.Nested(TaskStatusSchema, must_not_be_blank)
