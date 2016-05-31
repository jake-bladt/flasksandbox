import datetime
from app import bcrypt, db, login_manager

class User(db.Model):
  id = db.Column(db.Integer,  primary_key=True)
  email = db.Column(db.String(128), unique=True)
  password_hash = db.Column(db.String(255))
  user_name = db.Column(db.String(128), unique=True)
  is_active = db.Column(db.Boolean, default=True)
  created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
  modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

  readings = db.relationship('DailyReading', backref='daily_reading', lazy='dynamic')

  # Flask-Login interface
  def get_id(self):
    return str(self.id)

  def is_authenticated(self):
    return True

  def is_active(self):
    return self.active

  def is_anonymous(self):
    return False

  @staticmethod
  def make_password(plaintext):
    return bcrypt.generate_password_hash(plaintext)

  def check_password(self, raw_password):
    return bcrypt.check_password_hash(self.password_hash, raw_password)

  @classmethod
  def create(cls, email, password, **kwargs):
    return User(
      email=email,
      password_hash=User.make_password(password), **kwargs)

  @staticmethod
  def authenticate(email, password):
    user = User.query.filter(User.email == email).first()
    if user and user.check_password(password):
      return user
    return False

@login_manager.user_loader
def _load_user(user_id):
  return User.query.get(int(user_id))

class DailyReading(db.Model):
  id = db.Column(db.Integer,  primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  steps_count = db.Column(db.Integer)
  reading_day = db.Column(db.Date)
  notes = db.Column(db.String(255))
  created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
  modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

  def __repr__(self):
    return '<%n steps on %d>' % (self.steps_count, self.reading_day)
