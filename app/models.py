import datetime
from app import db

class DailyReading(db.Model):
  id = db.Column(db.Integer,  primary_key=True)
  steps_count = db.Column(db.Integer)
  reading_day = db.Column(db.Integer)
  notes = db.Column(db.String(255))
  created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
  modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)