from flask import render_template, redirect, url_for

from app import app, db
from models import DailyReading
from forms import StepsDataForm
from helpers import object_list

@app.route('/')
def homepage():
  readings = DailyReading.query.order_by(DailyReading.reading_day.desc())
  return object_list('homepage.html', readings, steps_form = StepsDataForm())

@app.route('/stepsreading', methods=['POST'])
def stepsreading():
  form = StepsDataForm(request.form)
  if form.validate():
    new_reading = form.populate_reading(DailyReading())
    existing_reading = session.query.filter(DailyReading.reading_day == new_reading.reading_day).first()
  else
    pass
