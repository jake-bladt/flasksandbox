from flask_wtf import Form
from wtforms import BooleanField, DateField, IntegerField, PasswordField, StringField, validators
from models import User

class StepsDataForm(Form):
  reading_day = DateField("Reading Date", [validators.Required()], format='%m/%d/%y')
  steps_count = IntegerField("Steps", [validators.Required()])

  def populate_reading(self, reading):
    self.populate_obj(reading)
    return reading

class LoginForm(Form):
  email = StringField("Email", validators=[validators.Required()])
  password = PasswordField("Password", validators=[validators.Required()])
  remember_me = BooleanField("Remember me?", default=True)

  def validate(self):
    if not super(LoginForm, self).validate():
      return False

    self.user = User.authenticate(self.email.data, self.password.data)
    if not self.user:
      self.email.errors.append("Invalid email or password.")
      return False

    return True
