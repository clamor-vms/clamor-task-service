from models.Model import db
from flask import Flask
from app import api_bp


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")

    app.run(host='0.0.0.0', port=80, debug=True)
