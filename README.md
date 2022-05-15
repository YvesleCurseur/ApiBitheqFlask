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
To execute your API locally, you need to create a `.env` file with the diferrents values: 

```bash
DB_ENGINE = ex(mysql,postrges,mariadb)
DB_PASSWORD = ex(yourdbpassword)
DB_USER = ex(localhost)
DB_PORT = ex(3306,5432)
DB_NAME = ex(bibliotheque)
FLASK_APP = app.py
FLASK_ENV = "development" to run localy, "production" for the deployment
```

Migration are optional in this case but for launch the migrations to create your database. These migrations are managed using the following commands:
- flask db init
- flask db migrate -m "Initial migration."
- python manage.py db upgrade.