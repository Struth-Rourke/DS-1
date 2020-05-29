# Installation Instructions for Dependencies (pipenv, Mac/Linux)

## Flask, Flask-Cors, Psycopg2, Gunicorn, Requests, Dotenv
```sh
pipenv install Flask flask-cors psycopg2-binary gunicorn requests python-dotenv
```
## PostgreSQL Database Connection
Example of format to place credentials inside a .env file:
```py
DB_USER="database-user"
DB_NAME="database-name"
DB_PASSWORD="database-password"
DB_HOST="database-server-domain.com"
```

# Heroku Deployment
- Add "Procfile" with following content:
```sh
web: gunicorn "salty_app:create_app()"
```
- Log in to Heroku from the CLI (first time only):
```sh
heroku login
```
- Creating a new application server (MUST BE DONE FROM WITHIN THE REPOSITORY'S ROOT DIRECTORY):
```sh
git remote -v
heroku create # optionally provide a name... "heroku create my-app-name"
git remote -v
```
- Deploying to Production:
```sh
git push heroku master
```
- Viewing production app in browser:
```sh
heroku open
```
- Checking production server logs:
```sh
heroku logs --tail
```
- Configuring production environment variables:
```sh
heroku config: set DB_USER="___________"
heroku config: set DB_NAME="___________"
heroku config: set DB_PASSWORD="___________"
heroku config: set DB_HOST="___________"
```