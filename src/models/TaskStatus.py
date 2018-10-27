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
from flask_sqlalchemy import SQLAlchemy
from models import db
# db = SQLAlchemy()


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
