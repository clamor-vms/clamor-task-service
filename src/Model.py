from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


# Schemas ***************************
class TaskSchema(ma.Schema):
    __tablename__ = 'tasks'
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    task_group_id = fields.Integer()
    # userid = db.Column(sa.Integer, db.ForeignKey('user.id'))


class TaskGroupSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    tasks = fields.List(fields.Nested(TaskSchema()))


# Models *****************************
class TaskGroup(db.Model):
    __tablename__ = 'taskGroups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)
    tasks = db.relationship("Task", back_populates="taskGroups")

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)
    task_group_id = db.Column(db.Integer, db.ForeignKey('taskGroup.id'))
    taskGroup = db.relationship("TaskGroup", back_populates="taskGroups")

    def __init__(self, name, description, task_group_id):
        self.name = name
        self.description = description
        self.task_group_id = task_group_id
#
#
#
#
