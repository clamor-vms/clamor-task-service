# Setup

Establish a virtual env, with package `virtualenv`, in the command line with `virtualenv <yourEnvName>`. Next, activate the virtual environment with (for linux) `source <yourName>/bin/activate` to activate it. If you're running on windows, check out [this guide on running python virtual environments.](https://virtualenv.pypa.io/en/stable/userguide/)

after this, install all the packages from the requirements.txt file. you can install all dependancies with `pip install -r requirements.txt`.

There is a config.dev.py file in the `src` directory - the name of this file will need to be changed to `config.py` and you will need to input your computer local variables in the database information to get the project up and running.

## Migration

To set up the migrations for this project manually (and not run through docker command) you will need to run the commands in order : `python migrate.py db init`, `python migrate.py db migrate`, and finally `python migrate.py db upgrade` from the `migrate.py` file in the src directory.
