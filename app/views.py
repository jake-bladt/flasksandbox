from flask import Blueprint
from flask import render_template
from helpers import object_list
from models import DailyReading

from app import app

@app.route('/')
def homepage():
  readings = DailyReading.query.order_by(DailyReading.reading_day.desc())
  return object_list('homepage.html', readings)
