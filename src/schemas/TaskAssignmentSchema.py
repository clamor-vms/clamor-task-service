from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from models import ma


class TaskAssignmentSchema(ma.Schema):
    id = fields.Integer()
    start_date = fields.Date()
    end_date = fields.Date()
    user_id = fields.Integer()
    task_id = fields.Integer(required=True)
