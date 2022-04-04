import os

SECRET_KEY = os.urandom(32)

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:SecretPassw0rd@localhost:5432/bibliotheque" 

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False