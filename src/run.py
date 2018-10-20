from models.Model import db
from flask import Flask
from app import api_bp
from models import TaskStatus
from schemas import TaskStatusSchema

app = Flask(__name__)
task_statuses_schema = TaskStatusSchema(many=True)
task_status_schema = TaskStatusSchema()

taskStatuses = [
    TaskStatus("Needs Assignment", "new", True, True, True),
    TaskStatus("Ready To Start", "assigned", False, False, False),
    TaskStatus("In Review", "in_review", False, False, False),
    TaskStatus("Completed", "completed", False, True, False),
    TaskStatus("Cancelled", "cancelled", False, False, True)
]


def create_app(config_filename):
    app.config.from_object(config_filename)
    app.register_blueprint(api_bp, url_prefix='')

    db.init_app(app)

    return app


@app.before_first_request
def seed_database():
    from models import db
    status = TaskStatus.query.all()
    if not status:
        print("no task statuses found, seeding status data...")
        for status in taskStatuses:
            print(status)
            db.session.add(status)
            db.session.commit()
        print("Task statuses added to database.")


if __name__ == "__main__":
    app = create_app("config")

    app.run(host='0.0.0.0', port=80, debug=True)
