from flask import redirect, render_template, request, url_for

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
  print(form.reading_day)
  if form.validate():
    new_reading = form.populate_reading(DailyReading())
    existing_reading = DailyReading.query.filter(DailyReading.reading_day == new_reading.reading_day).first()
    if existing_reading:
      print("Updating reading for " + existing_reading.reading_day)
      existing_reading.steps_count = new_reading.steps_count
    else:
      print("Creating new reading for " + new_reading.reading_day)
      db.session.add(new_reading)
    db.session.commit()
  else:
    print("form failed to validate.")
    print(form.errors)

  return redirect(url_for('homepage'))
