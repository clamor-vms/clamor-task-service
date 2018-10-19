from flask import Flask
from app import api_bp


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from models import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")

    migrate = migrate(app, db)
    manager = manager(app)
    manager.add_command('db', migratecommand)
    manager.run()

    app.run(host='0.0.0.0', port=80, debug=True)
