import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Take Models, Views from directory Flask_MVC
from flask_mvc.models import db
from flask_mvc.views import the_path

# For env
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
# And if you whant to separe this part
# app.config.from_object('config')

SECRET_KEY = os.urandom(32)

# Enable debug mode.
DEBUG = True
if os.environ.get("ENV") == "PRODUCTION":
    DEBUG = False
else:
    DEBUG = True

# Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.getenv('ENGINE')}://{os.getenv('DB_ENGINE')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_USER')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Turn off the Flask-SQLAlchemy event system and warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Use of blueprint for the path
app.register_blueprint(the_path, url_prefix='/')
