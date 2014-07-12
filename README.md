#Yet Another Flask Boilerplate Repo.

###About

Flask is a micro framework, and this is a micro Flask setup.

The repo. contains just enough to get a new Flask + SQLAlchemy app off the ground. No Bootstrap, etc. It's like [micro flask](https://github.com/tayler/micro-flask) but not quite as micro.

I'm new to Flask and Python, and I wanted a decent starting point for new Flask apps, something where I understood all the moving parts.

The app structure setup is mostly from the Package structure in [Explore Flask](http://exploreflask.com/organizing.html#organization-patterns), but some stuff was filled in from the Flask tutorial at [Real Python](http://www.realpython.com/blog/python/python-web-applications-with-flask-part-i/).

The SQLAlchemy setup is a synthesis from a number of sources (thanks to to them for writing all of this down):
    - http://flask.pocoo.org/docs/patterns/sqlalchemy/  
    - https://pythonhosted.org/Flask-SQLAlchemy/quickstart.html  
    - http://www.realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/  
It is setup in the declarative style, so some tutorials will be different than what you see here.

###Project Structure

```sh
├── README.md
├── config.py (configuration that is not environment specific. Config values set in instance/config.py override those set in this config.py)
├── instance/ (config. that should not be in version control, e.g., sensitive creds. and/or environment specific variables like `DEBUG`)
│   └── config.py
├── requirements.txt
├── run.py (used only in development. Test site with `python run.py`. You need to modify the `import` statement around line 5 to match the name of the package)
└── yourappname/ (change to the name of your app)
    ├── __init__.py
    ├── forms.py
    ├── models.py
    ├── static/
    │	├── img
    │   ├── js
    │   │   ├── main.js
    │   │   └── vendors/
    │   └── style
    │       └── main.css
    ├── templates/
    │   ├── home.html (very, very basic home page template)
    │   └── layout.html (very basic layout file)
    └── views.py
```

See [Explore Flask](http://exploreflask.com/organizing.html#organization-patterns) for more setup possibilities.

###Flask Setup

1. Clone this repo
2. Change package name directory (currently yourappname) to the name of your app
3. Repeat for the `import` statement in run.py, in models.py, and in the `init_db` function in database.py
4. Setup virtualenv for this directory & activate (because I always forget, virtualenvwrapper command is `mkvirtualenv <env-name>`)
5. Create an `instance/` dir containing a `config.py` file in the root directory
6. `pip install -r requirements.txt`

####SQLAlchemy Setup
1. Change database URI in `config.py` where `SQLALCHEMY_DATABASE_URI` is declared (see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html for possibilities)
2. Define your models in `yourappname/models.py`
3. Get your database tables set up (With Postgresql, I found out you have to set up your database before you can `init_db()`. Other DB engines might be different.):
4. Create db in psql (or elsewhere): `CREATE DATABASE projproj;`
5. Run these commands in root of project dir to create tables based on your models:  
    a. `python`  
    b. `from yourappname.database import init_db`  
    c. `init_db()` (this should create the tables defined in the models. The models are imported in `init_db()` in `database.py`)  
6. Check that SQLAlchemy created your tables (can use psql or some other tool; in psql, the command to see the tables is `\c yourappdatabase \dt`)
7. `python run.py`
8. Navigate to 127.0.0.1:5000 in your browser to test it out
