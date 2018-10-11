from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from Model import db, ma


class TaskGroupSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    tasks = fields.List(fields.Nested(TaskSchema()))


class TaskGroup(db.Model):
    __tablename__ = 'taskGroups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)
    tasks = db.relationship("Task", back_populates="taskGroups")

    def __init__(self, name, description):
        self.name = name
        self.description = description
