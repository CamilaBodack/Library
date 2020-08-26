# Library

## Running the project


- Docker on linux

Open prompt in the root of project and execute the following commands:

```
docker-compose build
docker-compose run web python manage.py createsuperuser
docker-compose up
```

- Available in http://127.0.0.1:8000/admin/
- Login with created user

- Without docker:
- **better run this project inside virtualenv**
- Install requirements.txt
- In root of project run:

```
python manage.py createsuperuser
python manage.py runserver
```

- Available in http://127.0.0.1:8000/admin/
- Login with created user



## Docs:
- Swagger: http://127.0.0.1:8000/doc
- Redoc: http://127.0.0.1:8000/redoc
