import os

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Take Models, Views from directory Flask_MVC
from src.models import db
from src.views import chemin

# For env
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
# And if you whant to separe this part
# app.config.from_object('config')

app.config['SECRET_KEY'] = os.urandom(25)

# Enable debug mode.
DEBUG = True
if os.environ.get("ENV") == "PRODUCTION":
    DEBUG = False
else:
    DEBUG = True

# Connect to the database
# app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.getenv('ENGINE')}://{os.getenv('DB_ENGINE')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_USER')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# for heroku deploy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uomsdzpmortbsg:60ea30be28f763eed40fbe79627957cf80dea24d5acd2f809138ce30b053fd9d@ec2-3-224-164-189.compute-1.amazonaws.com:5432/dfspipb7i3evij'

# Turn off the Flask-SQLAlchemy event system and warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Blueprint can be use for the path, directory, templates etc to split the flask app and make different type for components
app.register_blueprint(chemin)

#Return errors into json
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "Success": False,
        "Error": 400,
        "Message": "Bad request !"
        }), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "Success": False,
        "Error": 404,
        "Message": "Not found !"
        }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "Success": False,
        "Error": 405,
        "Message": "Method not allowed !"
        }), 405

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "Success": False,
        "Error": 500,
        "Message": "Internal server error !"
        }), 500