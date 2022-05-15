# ApiBitheqFlask
## Summary
1. Why ?
2. Directory and project environment
3. Setup the project
4. API Documentation

## Why ?
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

- **controllers.py**: Define all my functions to manage the api

- **models.py**: Contains The class for the database

- **views.py**: Setup all the route for the functions 

- **app.py**: With all my flask app config, and specially a `blueprint` config who allows to split the project

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
```bash   
https://apibitheqflask.herokuapp.com/categorie
```
- Offline   
```bash 
http://localhost:5000/categorie
```

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
        
### GET/category/id
This endpoint allows you to get a particular category using his id, success value, total category of book.

- Online  
```bash   
https://apibitheqflask.herokuapp.com/categorie/1
```
- Offline   
```bash 
http://localhost:5000/categorie/1
```
= Results =

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
- Online  
```bash   
https://apibitheqflask.herokuapp.com/categorie
```

- Offline  
```bash   
http://localhost:5000/categorie
```
= Results =

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
- Online  
```bash   
https://apibitheqflask.herokuapp.com/categorie/6
```
- Offline   
```bash 
http://localhost:5000/categorie/6
```
= Results =

    {
        "Categorie": {
            "Libelle Categorie": "Update",
            "id": 6
        },
        "Nombre categorie": 6,
        "Success": true
    }

### DELETE/category/id
This endpoints remove a specific category, return success value, total number of category. 
- Online  
```bash   
    https://apibitheqflask.herokuapp.com/categorie/6
```
- Offline   
```bash 
    http://localhost:5000/categorie/6
```
= Results =

    {
        "Nombre Categorie": 5,
        "Success": true,
        "id supprime": 6
    }

### GET/book
This endpoints returns a list of book, success value, total number of book. 

- Online  
```bash   
https://apibitheqflask.herokuapp.com/livre
```
- Offline   
```bash 
http://localhost:5000/livre
```

= Results =

    {
        "Livres": [
            {
                "Auteur": "Rodrige",
                "Categorie": 1,
                "Date publication": "Wed, 13 Dec 2000 00:00:00 GMT",
                "Editeur": "Nathan",
                "Titre": "Mes aveux",
                "id": 1,
                "isbn": "48205842"
            },
            {
                "Auteur": "Nobel",
                "Categorie": 1,
                "Date publication": "Mon, 07 May 1990 00:00:00 GMT",
                "Editeur": "Les montagnes",
                "Titre": "Rédemption",
                "id": 2,
                "isbn": "462642642"
            },
            {
                "Auteur": "Robinson",
                "Categorie": 2,
                "Date publication": "Tue, 17 Oct 1905 00:00:00 GMT",
                "Editeur": "Monaco",
                "Titre": "Les refuges de Némos",
                "id": 3,
                "isbn": "979426724"
            },
            {
                "Auteur": "Coléoptère",
                "Categorie": 3,
                "Date publication": "Fri, 29 Apr 2005 00:00:00 GMT",
                "Editeur": "Brézilness",
                "Titre": "Finition",
                "id": 4,
                "isbn": "590638563"
            },
            {
                "Auteur": "Revenir",
                "Categorie": 3,
                "Date publication": "Sun, 12 Aug 1945 00:00:00 GMT",
                "Editeur": "Constructor",
                "Titre": "Sex on the beach",
                "id": 5,
                "isbn": "9030405735"
            }
        ],
        "Nombre Livre": 5,
        "Success": true
    }
        
### GET/book/id
This endpoint allows you to get a particular book using his id, success value, total number of book.

- Online  
```bash   
https://apibitheqflask.herokuapp.com/livre/1
```
- Offline   
```bash 
http://localhost:5000/livre/1
```
= Results =

    {
        "Livre": [
            {
                "Auteur": "Rodrige",
                "Categorie": "Sci-fi",
                "Date publication": "Wed, 13 Dec 2000 00:00:00 GMT",
                "Editeur": "Nathan",
                "Titre": "Mes aveux",
                "id": 1,
                "id categorie": 1,
                "isbn": "48205842"
            }
        ],
        "Nombre Livre": 5,
        "Success": true
    }

### POST/book
This endpoint allows you to create a book, return it, the success value and the total number of book.
- Online  
```bash   
https://apibitheqflask.herokuapp.com/livre
```

- Offline  
```bash   
http://localhost:5000/livre
```
= Results =

    {
        "Livre": [
            {
                "Auteur": "Rodrige",
                "Categorie": 1,
                "Date publication": "Wed, 13 Dec 2000 00:00:00 GMT",
                "Editeur": "Nathan",
                "Titre": "Mes aveux",
                "id": 1,
                "isbn": "48205842"
            },
            {
                "Auteur": "Nobel",
                "Categorie": 1,
                "Date publication": "Mon, 07 May 1990 00:00:00 GMT",
                "Editeur": "Les montagnes",
                "Titre": "Rédemption",
                "id": 2,
                "isbn": "462642642"
            },
            {
                "Auteur": "Robinson",
                "Categorie": 2,
                "Date publication": "Tue, 17 Oct 1905 00:00:00 GMT",
                "Editeur": "Monaco",
                "Titre": "Les refuges de Némos",
                "id": 3,
                "isbn": "979426724"
            },
            {
                "Auteur": "Coléoptère",
                "Categorie": 3,
                "Date publication": "Fri, 29 Apr 2005 00:00:00 GMT",
                "Editeur": "Brézilness",
                "Titre": "Finition",
                "id": 4,
                "isbn": "590638563"
            },
            {
                "Auteur": "Revenir",
                "Categorie": 3,
                "Date publication": "Sun, 12 Aug 1945 00:00:00 GMT",
                "Editeur": "Constructor",
                "Titre": "Sex on the beach",
                "id": 5,
                "isbn": "9030405735"
            },
            {
                "Auteur": "Fulbert",
                "Categorie": 5,
                "Date publication": "Sun, 15 May 2022 00:00:00 GMT",
                "Editeur": "Yves_le_Curseur",
                "Titre": "For the test",
                "id": 6,
                "isbn": "1"
            }
        ],
        "Nombre Livre": 6,
        "Success": true,
        "id Livre": 6
    }

### PATCH/book/id
This endpoints update aspecific book, return success value, total number of book. 
- Online  
```bash   
https://apibitheqflask.herokuapp.com/livre/6
```
- Offline   
```bash 
http://localhost:5000/livre/6
```
= Results =

    {
        "Livre": {
            "Auteur": "Fulbert 2.0",
            "Categorie": 5,
            "Date publication": "Sun, 15 May 2022 00:00:00 GMT",
            "Editeur": "Yves_le_Curseur 2.0",
            "Titre": "Update",
            "id": 6,
            "isbn": "2"
        },
        "Nombre Livre": 6,
        "Success": true
    }

### DELETE/book/id
This endpoints remove a specific book, return success value, total number of book. 
- Online  
```bash   
    https://apibitheqflask.herokuapp.com/livre/6
```
- Offline   
```bash 
    http://localhost:5000/livre/6
```
= Results =

    {
        "Id Livre": 6,
        "Nombre Livre": 5,
        "Success": true
    }

### GET/book/category/id
This endpoint allows you to get all the books of a specifics category using his id, success value, total category of book.

- Online  
```bash   
https://apibitheqflask.herokuapp.com/livre/categorie/1
```
- Offline   
```bash 
http://localhost:5000/livre/categorie/1
```
= Results =

    {
        "Livre": [
            {
                "Auteur": "Rodrige",
                "Categorie": 1,
                "Date publication": "Wed, 13 Dec 2000 00:00:00 GMT",
                "Editeur": "Nathan",
                "Titre": "Mes aveux",
                "id": 1,
                "isbn": "48205842"
            },
            {
                "Auteur": "Nobel",
                "Categorie": 1,
                "Date publication": "Mon, 07 May 1990 00:00:00 GMT",
                "Editeur": "Les montagnes",
                "Titre": "Rédemption",
                "id": 2,
                "isbn": "462642642"
            }
        ],
        "Nombre Livre": 5,
        "Success": true
    }

### Another results you can get

    {
        "Message": "Le livre n'existe pas !",
        "Success": false
    }

    {
        "Message": "Le code isbn existe déjà !",
        "Success": false
    }
