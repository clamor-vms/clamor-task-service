import os

# docker example:
# docker run --name clamour -e MYSQL_ROOT_PASSWORD=your-secret-pw
# -e MYSQL_DATABASE=task -p 3306:3306 -d mysql:5.7
# You need to replace the next values with
# the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://username:password@127.0.0.1/database_name"
