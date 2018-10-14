from flask import Flask
from .Model import db
from .TaskSchema import TaskSchema
from .Task import Task


class TaskGroup(db.Model):
    __tablename__ = 'taskGroups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)
    tasks = db.relationship("Task", back_populates="taskGroup")

    def __init__(self, name, description):
        self.name = name
        self.description = description
