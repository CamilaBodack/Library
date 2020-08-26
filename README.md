# Library

Project modeled for bookstore implementation.

## Implementation

- Django 3.1
- djangorestframework 3.11.1


## Running the project


- Docker on linux

Open prompt in the root of project and execute the following commands:

```
docker-compose build
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up
```

- Available in http://127.0.0.1:8000/admin/
- Login with created user

- Without docker:

**better run this project inside virtualenv**
- Install requirements.txt
- In root of project run:

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Available in http://127.0.0.1:8000/admin/
- Login with created user

## Main Endpoints

Clients:
- http://127.0.0.1:8000/client


Books:
- http://127.0.0.1:8000/books



## Docs:

To see all endpoints and test:

- Swagger: http://127.0.0.1:8000/doc
- Redoc: http://127.0.0.1:8000/redoc

## Tests

In root DIR, open console and run:
```
python manage.py test
```
