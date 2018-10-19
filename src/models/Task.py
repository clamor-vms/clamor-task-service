from flask import Flask
from schemas import TaskStatusSchema
from .Model import db
from models import TaskStatus


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)
    task_group_id = db.Column(db.Integer, db.ForeignKey('taskGroups.id'))
    task_status_id = db.Column(db.Integer, db.ForeignKey("taskStatuses.id"))

    taskGroup = db.relationship("TaskGroup", back_populates="tasks")
    task_status = db.relationship("TaskStatus", foreign_keys=[task_status_id])
    assignments = db.relationship("TaskAssignment", back_populates="task")

    def __init__(self, name, description, task_group_id):
        self.name = name
        self.description = description
        self.task_group_id = task_group_id
