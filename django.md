# Django

1. `mkdir <new-project>` > `cd <new-project>`
2. Virtual Environment: `python -m venv <venvname>`
3. Acticate the environment: `.\<venvname>\Scripts\activate.bat`
4. Install Django: `python -m pip install django`
5. Check Django version: `django-admin --version`
6. `django-admin startproject <my_project_name>`
7. Run the project: `cd <my_project_name>` > `python manage.py runserver`
8. Open your browser @ 127.0.0.1:8000
9. Create App: `python manage.py startapp <appname>`
10. `code .`

Database connection in `settings.py`:

```sh
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST': env('DATABASE_HOST'),
        'PORT': '3306',
    }
}
```


+ Run the site and hooking up the database:
```sh
myenv\Scripts\activate.bat
python manage.py makemigrations
py manage.py runserver
python manage.py migrate auth
python manage.py migrate
```

## Dockerize

+ The `Dockerfile`, also add a `requirements.txt` (Django==4.2.2) file:
```sh
FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install -r requirements.txt
RUN pip install pillow
RUN pip install django-bootstrap-v5
RUN pip install mysqlclient
RUN pip install django-environ


COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
```

The `docker-compose.yml` file (also add a `requirements.txt`)

```sh
version: "3.9"

services:
  django:
    image: django-hello-world:0.0.1
    build: .
    ports:
      - "8000:8000"
```

+ Build
```sh
docker compose up --build
docker build --tag sighthoundrescue:latest .
docker run --name sighthoundrescue -d -p 8000:8000 sighthoundrescue:latest
docker container ps

docker login
docker tag sighthoundrescue:latest sp00kysp00k/sighthoundrescue:latest
docker push sp00kysp00k/sighthoundrescue:latest
```
