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
from marshmallow import Schema, fields, pre_load, validate, post_load
from models import ma
from schemas import TaskAssignmentSchema, TaskStatusSchema, TaskGroupSchema

# Custom validator

# def must_not_be_blank(data):
#     if not data:
#         raise ValidationError('Foreign key not provided.')


class TaskSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    task_group_id = fields.Integer()
    task_status_id = fields.Integer()
    taskStatus = fields.Nested(
        'TaskStatusSchema', only=('code', 'name')
    )
    taskGroup = fields.Nested(
        'TaskGroupSchema', only=('name', 'description')
    )
    assignments = fields.Nested(
        'TaskAssignmentSchema', many=True
    )
    # assignments = fields.List(fields.Nested(TaskAssignmentSchema))
