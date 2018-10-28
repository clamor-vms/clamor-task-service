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
from .Task import Task
from .Model import db


class TaskGroup(db.Model):
    __tablename__ = 'taskGroups'
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer())
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(4055), unique=False, nullable=True)
    tasks = db.relationship("Task", back_populates="taskGroup")

    def __init__(self, name, description):
        self.name = name
        self.description = description
