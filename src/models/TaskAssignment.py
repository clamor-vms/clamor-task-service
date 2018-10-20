import datetime
from flask import Flask
from schemas import TaskSchema
from models import Task, db


class TaskAssignment(db.Model):
    __tablename__ = 'taskAssignments'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(
        'start_date',
        db.DateTime(),
        default=datetime.datetime.now
    )
    end_date = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer())
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    task = db.relationship("Task", back_populates="assignments")

    def __init__(self, task_id, user_id):
        self.task_id = task_id
        self.user_id = user_id
