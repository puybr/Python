# 🐍 Python

Created by _Guido van Rossum_, and released in 1991.

```py
# This is a comment
print("Hello, Friend!")
```

## Data Types
+ Text Type:	`str`
   + Concatenation of Strings: `FullName = Name + " " + Surname`
   + `"Python"` **Forward Indexing**: `0`, `1`, `2`, `3`, `4`, `5`
   + `"Python"` **Backward Indexing**: `-6`, `-5`, `-4`, `-3`, `-2`, `-1`
   + `len()`: `print(len("Hello World!"))`
   + Slice a string: `print(veryLongWord[0:5])`
   + Reverse a string using the slicing operator, `[::-1]`
   + String manipulation and functions: `astring.upper()`, `astring.lower()`, `astring.replace("$", " ")`, `astring.strip('*')`
+ Numeric Types:	`int`, `float`, `complex`
+ Sequence Types:	`list`, `tuple`, `range`
+ Mapping Type:	`dict`
+ Set Types:	`set`, `frozenset`
+ Boolean Type:	`bool`
+ Binary Types:	`bytes`, `bytearray`, `memoryview`

## Variables
A variable is created from the moment you assign a value to it

```py
x = 5
y = "String"
print(x)
print(y)
```

Variables to hold user input: `name = input("Enter your name: ")`

```py
name = input("What is your name?")
print("Hello, " + name + "!")
```

> There are 4 built-in data types used to store _collections_ of data: **List**, **Tuple**, **Set**, & **Dictionary**.

## Lists
List items are ordered, changeable, and allow duplicate values.

```py
mylist = ["orange", "pink", "green"]
```

## Tuples
A tuple is a collection of data which is ordered, unchangeable, and allows duplicate values.

```py
mytuple = ("orange", "pink", "green")
```

## Sets
Set items are unordered, unchangeable, and **do not** allow duplicate values.

```py
myset = {"orange", "pink", "green"}
```

## Dictionaries
Dictionary items are ordered, changeable, and does not allow duplicates. They are presented in `key:value` pairs, and can be referred to by using the key name.

```py
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

> Note: You can use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the `NumPy` library.

## Casting
Taking different types of data and converting them into different types for different purposes.
+ `str()` - converts an argument to a string
+ `int()` - converts an argument to an integer
+ `float()` - converts an argument to a float

```py
number = int(input("Please enter a number"))
answer = number * 10
print(str(number) + " x 10 = " + str(answer))
```
> The `print()` function can only work with string arguments. By default anything entered into an input is a string.

## Numbers

| Arithmetic Operations | Python Symbol |
|-----------------------|---------------|
| Addition              | +             |
| Subtraction           | -             |
| Multiplication        | *             |
| Division              | /             |
| Modulus               | %             |

# If Statements

```py
userInput = input("Enter your word here: ").lower()
forward = userInput
reverse = userInput[::-1]
if forward == reverse:
  print("Your word is a palindrome!")
else:
  print("Sorry, your word is not a palindrome!")
```

# Adding Python to `PATH` in `.vscode/settings.json`

```json
{
    "terminal.integrated.env.osx": {
      "PYTHONPATH": "${workspaceFolder}/libs",
    },
    "terminal.integrated.env.linux": {
      "PYTHONPATH": "${workspaceFolder}/libs",
    },
    "terminal.integrated.env.windows": {
      "PYTHONPATH": "${workspaceFolder}/libs",
    },
    "python.envFile": "${workspaceFolder}/.env"
}
```

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

There's a good starter tutorial [here](https://www.w3schools.com/django/index.php)
+ Database connection in `settings.py`:

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
python manage.py migrate auth
python manage.py migrate
python manage.py makemigrations
py manage.py runserver
```

# 🐋 Dockerize

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
docker build --tag <app_name>:latest .
docker run --name <app_name> -d -p 8000:8000 <app_name>e:latest
docker container ps

docker login
docker tag <app_name>:latest sp00kysp00k/<app_name>:latest
docker push sp00kysp00k/<app_name>:latest
```