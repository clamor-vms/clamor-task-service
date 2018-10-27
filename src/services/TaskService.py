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

from models import db, Task, TaskGroup, TaskStatus
from schemas import TaskSchema

tasks_schema = TaskSchema(many=True)
task_schema = TaskSchema()


class TaskService:
    """This is a Data access layer for the Task post methods."""

    def GetTasks(self):
        """Get all tasks."""
        tasks = Task.query.all()
        return tasks_schema.dump(tasks).data

    def GetTask(self, param):
        """Get single task."""
        taskGroup = TaskGroup.query.filter_by(id=param).first()
        return taskgroup_schema.dump(taskGroup).data

    def CreateTask(self, json_data):
        """Create new task."""
        # validate / deserialize input.
        data, errors = task_schema.load(json_data)
        if errors:
            err = {"message": errors}
            return {}, err

        # Check for valid task group
        task_group_id = TaskGroup.query.filter_by(
            id=data["task_group_id"]
        ).first()

        if not task_group_id:
            err = {"message": "Task group not found"}
            return {}, err

        # Check for valid task status
        task_status_id = TaskStatus.query.filter_by(
            id=data["task_status_id"]
        ).first()

        if not task_status_id:
            err = {"message": "You must enter a valid Task Status id."}
            return {}, err

        exists = Task.query.filter_by(name=data['name']).first()

        if exists:
            err = {'message': 'Task with that name already exists'}
            return {}, err

        task = Task(
            name=data["name"],
            description=data["description"],
            task_group_id=data["task_group_id"],
            task_status_id=data["task_status_id"]
        )

        db.session.add(task)
        db.session.commit()

        return task_schema.dump(task).data, None

    # def UpdateTask(self, json_data):
    #     """Update an existing task."""
    #     data, errors = taskgroup_schema.load(json_data)

    #     if errors:
    #         return {}, {'message': errors}

    #     taskGroup = TaskGroup.query.filter_by(id=data['id']).first()

    #     if not taskGroup:
    #         return {}, {'message': 'Task Group does not exist'}

    #     taskGroup.name = data['name']
    #     taskGroup.description = data['description']
    #     db.session.commit()

    #     return taskgroup_schema.dump(taskGroup).data, errors

    # def DeleteTask(self, json_data):
    #     """Delete existing task group."""
    #     data, errors = taskgroup_schema.load(json_data)
    #     if errors:
    #         return {}, errors

    #     taskGroup = TaskGroup.query.filter_by(id=data['id']).delete()
    #     db.session.commit()

    #     return taskgroup_schema.dump(taskGroup).data, errors
