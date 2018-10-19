from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, post_load
from models import ma


class TaskStatusSchema(ma.Schema):
    id = fields.Integer()
    code = fields.String(required=True)
    name = fields.String(required=True)
    isAssignmentNeeded = fields.Boolean()
    isCompleted = fields.Boolean()
    isCancelled = fields.Boolean()
