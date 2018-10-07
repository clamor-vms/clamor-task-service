import os

# You need to replace the next values with the appropriate values for your configuration
# update this file with your db requirements
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://username:password@localhost/task"
