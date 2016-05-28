import os

class Configuration(object):
  APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
  DEBUG = True
  SECRET_KEY = 'not really much of a secret'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/walker.db' % APPLICATION_DIR
  SQLALCHEMY_TRACK_MODIFICATIONS = True
