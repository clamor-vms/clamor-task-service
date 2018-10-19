from flask import Flask
from schemas import TaskSchema
from .Model import db


class TaskStatus(db.Model):
    __tablename__ = 'taskStatuses'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False)
    isAssignmentNeeded = db.Column(db.Boolean, default=True)
    isCompleted = db.Column(db.Boolean, default=True)
    isCancelled = db.Column(db.Boolean, default=True)

    def __init__(
        self,
        name,
        code,
        isAssignmentNeeded,
        isCompleted,
        isCancelled
    ):
        self.name = name
        self.code = code
        self.isAssignmentNeeded = isAssignmentNeeded
        self.isCompleted = isCompleted
        self.isCancelled = isCancelled
