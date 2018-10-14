from flask import Flask
from .Model import db


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)
    task_group_id = db.Column(db.Integer, db.ForeignKey('taskGroups.id'))
    taskGroup = db.relationship("TaskGroup", back_populates="tasks")

    def __init__(self, name, description, task_group_id):
        self.name = name
        self.description = description
        self.task_group_id = task_group_id
