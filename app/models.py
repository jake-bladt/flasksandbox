import datetime
from app import db

class User(db.Model):
  id = db.Column(db.Integer,  primary_key=True)
  email = db.Column(db.String(128), unique=True)
  password_hash = db.Column(db.String(255))
  user_name = db.Column(db.String(128), unique=True)
  is_active = db.Column(db.Boolean, default=True)
  created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
  modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

class DailyReading(db.Model):
  id = db.Column(db.Integer,  primary_key=True)
  steps_count = db.Column(db.Integer)
  reading_day = db.Column(db.Date)
  notes = db.Column(db.String(255))
  created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
  modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

  def __repr__(self):
    return '<%n steps on %d>' % (self.steps_count, self.reading_day)
