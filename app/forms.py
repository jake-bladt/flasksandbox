from flask_wtf import Form
from wtforms import DateField
from wtforms import IntegerField

class StepsDataForm(Form):
  reading_date = DateField("Reading Date")
  steps_count = IntegerField("Steps")

  def save_reading(self, reading):
    self.populate_object(reading)
    
