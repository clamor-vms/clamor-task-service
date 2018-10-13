from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from .Model import db, ma


class TaskSchema(ma.Schema):
    __tablename__ = 'tasks'
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    task_group_id = fields.Integer()


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)
    task_group_id = db.Column(db.Integer, db.ForeignKey('taskGroups.id'))

    def __init__(self, name, description, task_group_id):
        self.name = name
        self.description = description
        self.task_group_id = task_group_id
