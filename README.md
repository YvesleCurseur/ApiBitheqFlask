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
|----API_BIBLIOTHEQUE.postman_collection.json
|----app.py
|----README.md
|----requirements.txt    
```

- controllers.py 
Define all my functions to manage the api
- models.py
Contains The class for the database
- views.py
Setup all the route for the functions 
- app.py
With all my flask app config, and specially a `blueprint` config who allows me to split the project

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
FLASK_ENV = "development" to run localy, "production" to the deployment
```
 
You must then launch the migrations to create your database, spacialy the tables so create your database and run the following commands:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade.
```
Whant to know more about migrations? Check the [flask docs](https://flask-migrate.readthedocs.io/en/latest/).

You will then execute the commands to launch your API. To test all endpoints of your API, please use the `API_BIBLIOTHEQUE.postman_collection.json` file by importing it from Postman. If you don't have postman, you can download it from https://www.postman.com.

To run the server, execute:
`flask run` 


## API Documentation

This API has been deployed on heroku and is available from the link https://apibitheqflask.herokuapp.com

## Error Handling
Errors are retourned as JSON objects in the following format:
```bash
{
    "Success": False
    "Error": 400
    "Message": Bad request
}
```

The API will return four error types when requests fail:
- 400: Bad request
- 404: Not found
- 405: Method not allowed
- 500: Internal server error

## Endpoints

### GET/category
This endpoints returns a list of category, success value, total number of category. 

- Online    
`https://apibitheqflask.herokuapp.com/categorie`

- Offline    
`http://localhost:5000/categorie`

= Results =

    {
        "Categories": [
            {
                "Libelle Categorie": "Sci-fi",
                "id": 1
            },
            {
                "Libelle Categorie": "Art",
                "id": 2
            },
            {
                "Libelle Categorie": "Policier",
                "id": 3
            },
            {
                "Libelle Categorie": "Aventure",
                "id": 4
            },
            {
                "Libelle Categorie": "Enigme",
                "id": 5
            }
        ],
        "Nombre Categorie": 5,
        "Success": true
    }
        
### GET/category(categorie_id)
This endpoint allows you to get a particular category using his id. 
    
    https://apibitheqflask.herokuapp.com/categorie/1
    http://localhost:5000/categorie/1
    {
        "Categorie": {
            "Libelle Categorie": "Sci-fi",
            "id": 1
        },
        "Nombre categorie": 5,
        "Success": true
    }

### POST/category
This endpoint allows you to create a category.
    
    https://apibitheqflask.herokuapp.com/categorie
    http://localhost:5000/categorie
    {
        "Categorie": [
            {
                "Libelle Categorie": "Sci-fi",
                "id": 1
            },
            {
                "Libelle Categorie": "Art",
                "id": 2
            },
            {
                "Libelle Categorie": "Policier",
                "id": 3
            },
            {
                "Libelle Categorie": "Aventure",
                "id": 4
            },
            {
                "Libelle Categorie": "Enigme",
                "id": 5
            },
            {
                "Libelle Categorie": "test",
                "id": 6
            }
        ],
        "Nombre Categorie": 6,
        "Success": true
    }

### PATCH/category/id
This endpoints update aspecific category, return success value, total number of category. 

    https://apibitheqflask.herokuapp.com/categorie/6
    http://localhost:5000/categorie/6
    {
        "Categorie": {
            "Libelle Categorie": "Update",
            "id": 6
        },
        "Nombre categorie": 6,
        "Success": true
    }

### DELETE/category/6
This endpoints remove a specific categorie, return success value, total number of category. 

    https://apibitheqflask.herokuapp.com/categorie/6
    http://localhost:5000/categorie/6
    {
        "Nombre Categorie": 5,
        "Success": true,
        "id supprime": 6
    }

