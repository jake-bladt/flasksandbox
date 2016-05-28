from flask import render_template

from app import app
from models import DailyReading
from forms import StepsDataForm
from helpers import object_list

@app.route('/')
def homepage():
  readings = DailyReading.query.order_by(DailyReading.reading_day.desc())
  return object_list('homepage.html', readings, steps_form = StepsDataForm())

@app.route('/stepsreading')
def steps_reading():
  pass
