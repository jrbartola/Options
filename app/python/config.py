import os


def configure_app(app):
  configure_postgres(app)

def configure_postgres(app):
  user = os.environ['POSTGRES_USER']
  password = os.environ['POSTGRES_PASSWORD']
  host = os.environ['POSTGRES_HOST']
  database = os.environ['POSTGRES_DB']
  port = os.environ['POSTGRES_PORT']

  def make_db_uri():
    if 'DATABASE_URL' in os.environ: # Provided in a prod Heroku environment
      return os.environ['DATABASE_URL']
    return f'postgresql://{user}:{password}@{host}:{port}/{database}'
      
  DB_URI = make_db_uri() 
  app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.secret_key = os.urandom(32)
