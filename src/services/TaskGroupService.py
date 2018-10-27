"""
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
"""

from models import db, TaskGroup
from schemas.TaskGroupSchema import TaskGroupSchema

taskgroups_schema = TaskGroupSchema(many=True)
taskgroup_schema = TaskGroupSchema()


class TaskGroupService:
    """This is a Data access layer for the Task Group post methods."""

    def GetGroups(self):
        """Get all task groups."""
        taskgroups = TaskGroup.query.all()
        return taskgroups_schema.dump(taskgroups).data

    def GetGroup(self, param):
        """Get single task group."""
        taskGroup = TaskGroup.query.filter_by(id=param).first()
        return taskgroup_schema.dump(taskGroup).data

    def CreateGroup(self, json_data):
        """Create new task group."""
        data, errors = taskgroup_schema.load(json_data)
        err = None
        if errors:
            err = {
                'err': errors,
                'msg': 'Validation error',
                'tried': json_data
            }

        exists = TaskGroup.query.filter_by(name=data['name']).first()

        if exists:
            err = {'message': 'Task Group with that name already exists'}
            return {}, err

        taskGroup = TaskGroup(
            name=json_data['name'],
            description=json_data['description']
        )

        db.session.add(taskGroup)
        db.session.commit()

        return taskgroup_schema.dump(taskGroup).data, err

    def UpdateGroup(self, json_data):
        """Update an existing task group."""
        data, errors = taskgroup_schema.load(json_data)

        if errors:
            return {}, {'message': errors}

        taskGroup = TaskGroup.query.filter_by(id=data['id']).first()

        if not taskGroup:
            return {}, {'message': 'Task Group does not exist'}

        taskGroup.name = data['name']
        taskGroup.description = data['description']
        db.session.commit()

        return taskgroup_schema.dump(taskGroup).data, errors

    def DeleteGroup(self, json_data):
        """Delete existing task group."""
        data, errors = taskgroup_schema.load(json_data)
        if errors:
            return {}, errors

        taskGroup = TaskGroup.query.filter_by(id=data['id']).delete()
        db.session.commit()

        return taskgroup_schema.dump(taskGroup).data, errors
