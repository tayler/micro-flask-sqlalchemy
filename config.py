# http://exploreflask.com/configuration.html

# The config.py file should contain one variable assignment per line.
# When your app is initialized, the variables in config.py are configure
# these options are available to Flask and it's extensions via the app.config dictionary - e.g., app.config["DEBUG"]
# overridden by instance/config.py, if options are set here and there
DEBUG = False # Turns on debugging features in Flask
# see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html for info on how to configure the db uri
SQLALCHEMY_DATABASE_URI = 'postgresql://yourmachineuser@localhost/yourappdatabase'
