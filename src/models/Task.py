'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from flask import Flask
from schemas import TaskStatusSchema
from models import TaskStatus, TaskAssignment, db


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)

    task_group_id = db.Column(db.Integer, db.ForeignKey('taskGroups.id'))
    taskGroup = db.relationship("TaskGroup", back_populates="tasks")

    task_status_id = db.Column(db.Integer, db.ForeignKey("taskStatuses.id"))
    taskStatus = db.relationship("TaskStatus", foreign_keys=[task_status_id])

    assignments = db.relationship("TaskAssignment", back_populates="task")

    def __init__(self, name, description, task_group_id, task_status_id):
        self.name = name
        self.description = description
        self.task_group_id = task_group_id
        self.task_status_id = task_status_id
