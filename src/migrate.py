from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.Model import db
from run import create_app

app = create_app('config')

migrate = migrate(app, db)
manager = manager(app)
manager.add_command('db', migratecommand)


if __name__ == '__main__':
    manager.run()
