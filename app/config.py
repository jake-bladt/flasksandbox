class Configuration(object):
  APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/walker.db' % APPLICATION_DIR
  