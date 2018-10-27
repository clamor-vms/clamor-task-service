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

from models import db, TaskAssignment, Task
from schemas import TaskAssignmentSchema
from utilities import ValidEntry

task_assignments_schema = TaskAssignmentSchema(many=True)
task_assignment_schema = TaskAssignmentSchema()


class TaskAssignmentService:
    """This is a Data access layer for the Task Assignment Controller methods."""

    def GetAssignments(self):
        """Get all task groups."""
        assignments = TaskAssignment.query.all()
        return task_assignments_schema.dump(assignments).data

    def GetAssignment(self, param):
        """Get single task group."""
        assignment = TaskGroup.query.filter_by(id=param).first()
        return task_assignment_schema.dump(assignment).data

    def CreateAssignment(self, json_data):
        data, errors = task_assignment_schema.load(json_data)

        if errors:
            err = {'err': errors, 'msg': 'Validation error', 'tried': json_data}
            return {}, err

        if not ValidEntry(Task, id=data['task_id']):
            return {}, {'message': 'Task does not exist.'}

        taskAssignment = TaskAssignment(
            task_id=json_data['task_id'],
            user_id=json_data['user_id']
        )

        db.session.add(taskAssignment)
        db.session.commit()

        return task_assignment_schema.dump(taskAssignment).data, None

    def UpdateAssignment(self, json_data):
        data, errors = task_assignment_schema.load(json_data)

        if errors:
            return {}, errors

        if not "id" in data:
            err = {"message": "Task assignment ID is required."}
            return {}, err

        taskAssignment = ValidEntry(TaskAssignment, id=data['id'])

        if not taskAssignment:
            return {}, {'message': 'Task assignment does not exist'}

        taskAssignment.user_id = data['user_id']
        taskAssignment.task_id = data['task_id']
        db.session.commit()

        return task_assignment_schema.dump(taskAssignment).data, None

    def DeleteAssignment(self, json_data):
        data, errors = task_assignment_schema.load(json_data)

        if errors:
            err = {'err': errors, 'msg': 'Validation error', 'tried': json_data}
            return {}, err

        assignment = TaskAssignment.query.filter_by(id=data['id']).delete()
        db.session.commit()

        return task_assignment_schema.dump(taskGroup).data, None
