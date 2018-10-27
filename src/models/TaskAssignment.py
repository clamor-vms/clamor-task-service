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
