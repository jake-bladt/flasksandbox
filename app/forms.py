from flask_wtf import Form
from wtforms import DateField, IntegerField, validators
from models import User

class StepsDataForm(Form):
  reading_day = DateField("Reading Date", [validators.Required()], format='%m/%d/%y')
  steps_count = IntegerField("Steps", [validators.Required()])

  def populate_reading(self, reading):
    self.populate_obj(reading)
    return reading

class LoginForm(Form):
  email = wtforms.StringField("Email", validators=[validators.Required()])
  password = wtforms.PasswordField("Password", validators=[validators.Required()])
  remember_me = wtforms.BooleanField("Remember me?", default=True)
