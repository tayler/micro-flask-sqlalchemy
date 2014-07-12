# from http://flask.pocoo.org/docs/patterns/sqlalchemy/
# this follows the declarative pattern
from . import app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# Base is imported into yourappname/models.py
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import yourappname.models # import all models in yourappname/models.py
    Base.metadata.create_all(bind=engine)

# Flask will automatically remove database sessions at the end of the request or when the application shuts down
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
