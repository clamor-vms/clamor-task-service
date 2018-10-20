from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.Model import db
from run import create_app


taskStatuses = [
    TaskStatus("Needs Assignment", "new", True, True, True),
    TaskStatus("Ready To Start", "assigned", False, False, False),
    TaskStatus("In Review", "in_review", False, False, False),
    TaskStatus("Completed", "completed", False, True, False),
    TaskStatus("Cancelled", "cancelled", False, False, True)
]


app = create_app('config')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
