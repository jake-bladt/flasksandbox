from flask_wtf import Form
from wtforms import DateField, IntegerField, validators

class StepsDataForm(Form):
  reading_day = DateField("Reading Date", [validators.DataRequired()])
  steps_count = IntegerField("Steps", [validators.DataRequired()])

  def populate_reading(self, reading):
    self.populate_object(reading)
    return reading
