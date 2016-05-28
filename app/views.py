from flask import render_template
from models import DailyReading

from app import app
from helpers import object_list

@app.route('/')
def homepage():
  readings = DailyReading.query.order_by(DailyReading.reading_day.desc())
  return object_list('homepage.html', readings)
