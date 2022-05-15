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
<!-- 
Migration are optional in this case but for launch the migrations to create your database run the following commands:
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
{
    "Success": False
    "Error": 400
    "Message": Bad request
}

The API will return four error types when requests fail:
. 400: Bad request
. 404: Not found
. 405: Method not allowed
. 500: Internal server error

## Endpoints

### GET/movies
    GENERAL: 
        This endpoints returns a list of movies object, success value, total number of the movies. 

            Sample: curl https://capstoneapi.herokuapp.com/movies

            {
                "movies": [
                    {
                        "id": 1,
                        "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                        "title": "Thomas NGIJOL"
                    },
                    {
                        "id": 3,
                        "release_date": "Wed, 02 Dec 2020 00:00:00 GMT",
                        "title": "Casanova"
                    }
                ],
                "success": true,
                "total_movies": 2
            }

###  GET/movies(movie_id)
    GENERAL: This endpoint allows you to get for a particular Movie using its id. This endpoint
     returns one movie, and the status_code
            Sample: curl https://capstoneapi.herokuapp.com/movies/1

            {
                "movie": [
                    {
                        "id": 1,
                        "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                        "title": "Thomas NGIJOL"
                    }
                ],
                "success": true
            }

###  GET/actors
    GENERAL: 
        This endpoints returns a list of actors object, success value, total number of the actors. 

            Sample: curl https://capstoneapi.herokuapp.com/actors

            {
                "actors": [
                    {
                        "age": 32,
                        "gender": "M",
                        "id": 1,
                        "name": "Badiou OURO"
                    },
                    {
                        "age": 45,
                        "gender": "M",
                        "id": 5,
                        "name": "Jamel Debouzze"
                    }
                ],
                "success": true
            }

###  GET/actors(actor_id)
    GENERAL: This endpoint allows you to get for a particular actor using its id. This endpoint 
    returns one actor, and the status_code
            Sample: curl https://capstoneapi.herokuapp.com/actors/1

            {
                "actor": [
                    {
                        "age": 32,
                        "gender": "M",
                        "id": 1,
                        "name": "Badiou OURO"
                    }
                ],
                "success": true
            }


###  DELETE/actors(actor_id)
    GENERAL: Delete the actor  of the given ID if it exists. Return the id of the deleted actor, 
    success value, total of actors and actor list based on current page number. Results are paginated in groups of 10.

            Sample: curl - X DELETE https://capstoneapi.herokuapp.com/actors/5
            {
                "actors": [
                    {
                        "age": 32,
                        "gender": "M",
                        "id": 1,
                        "name": "Badiou OURO"
                    }
                ],
                "deleted": 5,
                "success": true,
                "total_actors": 1
            }


        ###  DELETE/movies(movie_id)
            GENERAL: Delete the movie  of the given ID if it exists. Return the id of the deleted movie, 
            success value, total of movies and movies list based on current page number. Results are
             paginated in groups of 10.

            Sample: curl - X DELETE https://capstoneapi.herokuapp.com/movies/5

            {
        "actors": [
            {
                "id": 1,
                "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                "title": "Thomas NGIJOL"
            }
        ],
        "deleted": 3,
        "success": true,
        "total_movies": 1
    }


###  POST/movies
    GENERAL: This endpoint is used to create a new movie. We return the ID of the new movie created, 
    the movie that was created, the list of movies and the number of movies.

            Sample: curl -X POST https://capstoneapi.herokuapp.com/movies 
            -H "Content-Type:application/json" -d "{"title":"Casanova","release_date":"2020-12-02"}"

                {    
            "movies": [
                {
                    "id": 1,
                    "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                    "title": "Thomas NGIJOL"
                },
                {
                    "id": 4,
                    "release_date": "Wed, 02 Dec 2020 00:00:00 GMT",
                    "title": "Casanova"
                }
            ],
            "created": 4,
            "success": true,
            "total_movies": 2
            }



###  POST/actors
    GENERAL: This endpoint is used to create a new actor. We return the ID of the new actor 
    created, the movie that was created, the list of actors and the number of actors.

            Sample: curl -X POST https://capstoneapi.herokuapp.com/actors 
            -H "Content-Type:application/json" -d "{"name":"Jamel Debouzze","age":45,"gender":"M"}"

                {
                    "actors": [
                        {
                            "age": 32,
                            "gender": "M",
                            "id": 1,
                            "name": "Badiou OURO"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 6,
                            "name": "Jamel Debouzze"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 7,
                            "name": "Jamel Debouzze"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 8,
                            "name": "Jamel Debouzze"
                        }
                    ],
                    "created": 8,
                    "success": true,
                    "total_actors": 4
                }
 -->
