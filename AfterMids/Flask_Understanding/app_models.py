from app_run import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import column, Integer

models = SQLAlchemy(app)

class Users(models.Model):
    pass