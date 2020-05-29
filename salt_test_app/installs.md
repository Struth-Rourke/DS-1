# Installation Instructions for Dependencies (pipenv, Mac/Linux)

## Flask, Flask-Cors, Psycopg2, Gunicorn, Requests, Dotenv
```sh
pipenv install Flask flask-cors psycopg2-binary gunicorn requests python-dotenv
```
## Flask-Cors
```sh
pipenv install flask-cors
```
## Psycopg2
```sh
pipenv install psycopg2-binary
```
## Gunicorn (for Heroku deployment)
```sh
pipenv install gunicorn
```
## Requests
```sh
pipenv install requests
```
## Dotenv
```sh
pipenv install python-dotenv
```
## PostgreSQL Database Connection
Example of format to place credentials inside a .env file:
```py
DB_USER="database-user"
DB_NAME="database-name"
DB_PASSWORD="database-password"
DB_HOST="database-server-domain.com"
```