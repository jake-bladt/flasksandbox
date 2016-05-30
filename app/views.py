from flask import redirect, render_template, request, url_for

from app import app, db
from models import DailyReading
from forms import StepsDataForm, LoginForm
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
    existing_reading = DailyReading.query.filter(DailyReading.reading_day == new_reading.reading_day).first()
    if existing_reading:
      existing_reading.steps_count = new_reading.steps_count
    else:
      db.session.add(new_reading)
    db.session.commit()

  return redirect(url_for('homepage'))

@app.route("/login/", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    form = LoginForm(request.form)
    if form.validate():
      login_user(form.user, remember=form.remember_me.data)
      return redirect(request.args.get("next") or url_for("homepage"))
  else:
    form = LoginForm()

    return render_template("login.html", form=form)
