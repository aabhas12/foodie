# Foodie
> Backend For Food Recipe Sharing Application

## Contents
- [Tech-stack used](#tech-stack-used)
- [Getting Started](#getting-started)
    - [Cloning](#1-cloning)
    - [pipenv installation](#2-pipenv-installation)
    - [Install dependencies](#3-install-dependencies)
    - [pipenv activation](#4-pipenv-activation)
    - [Migrate](#5-migrate)
    - [Run development server](#6-run-development-server)
- [API Documentation](#api-documentation)

## Tech-stack used
- Python 3.7
- Django 2.2

## Getting Started
Here are the steps to setup development environment
### 1. cloning
Clone the repository on your local machine.
```sh
git clone https://github.com/aabhas12/foodie.git
```

### 2. pipenv installation
We use pipenv for managing virtual environment. Execute this command to install pipenv.
```sh
pip3 install pipenv
```

### 3. Install Dependencies
Install project dependencies. All the dependencies are specified in Pipfile (Versions are in Pipfile.lock)
```sh
pipenv install
```

### 4. pipenv activation
Activate virtual environment.
```sh
pipenv shell
```

### 5. Migrate
Run migrate to make structure changes on new database.
```sh
python manage.py migrate
```

### 6. Run development server
Either click run on IDE (Pycharm) or run this command on terminal:
```sh
python manage.py runserver
```
You will see success message with URL its working on.

## API Documentation
All the API endpoints and payload information, response formats can be found after running the server on 
https://localhost:8000/redoc<br />
Used the library drf-yasg for this
