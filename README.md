# ApiBitheqFlask
## Summary
1. Motivation
2. Directory and project environment
3. Setup the project
4. API Documentation



## Motivation
This is a Flask API project for managing books is, this project aims knowing this following concepts :
- Modeling of the database for a web application using the SQLAlchemy ORM (src/models.py)
- CRUDs to interact with the database: (src/controllers.py)
- Deployment on heroku (Procfile, setup.sh)

## Directory and project environment

```bash
Apibitheqflask/
|
|----migrations/
|
|----src/
|    |----controllers.py
|    |----models.py
|    |----views.py
|
|----.gitignore
|----app.py
|----README.md
|----requirements.txt    
```
### Dependencies

#### Python
Python 3.9.10
Follow instructions to install the latest version of python for your sepecific platform by following this: [install python](https://realpython.com/installing-python/).

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment: [create a virtual environement](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, before install dependencies be sure to be in the directory of the project ```/Apibitheqflask ``` and run:
```bash
pip install -r requirements.txt
```
Heroku looks for a requirements.txt file that needs to include all of your dependencies.

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server locally
To execute your API locally, you need to modify create a `.env` file with the diferrents values: 
```bash
ENGINE=postgresql
DB_ENGINE=postgres
DB_PASSWORD=SecretPassw0rd
DB_USER=localhost
DB_PORT=5432
DB_NAME=bibliotheque
FLASK_APP=app.py
FLASK_ENV=development
```

You must then launch the migrations to create your database. These migrations are managed using the following commands:
- python manage.py db init
- python manage.py db migrate
- python manage.py db upgrade.