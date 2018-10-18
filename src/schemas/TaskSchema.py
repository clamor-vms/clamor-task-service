from flask import Flask
from models import ma
from marshmallow import Schema, fields, pre_load, validate


class TaskSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    task_group_id = fields.Integer()
