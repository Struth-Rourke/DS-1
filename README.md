# DS

## Resources
- Postgres Database
- VADER Sentinment Analysis
- Flask
- Heroku  

## Installation Instructions for Dependencies (pipenv, Mac/Linux)

- Flask, Flask-Cors, Psycopg2, Gunicorn, Requests, Dotenv
```sh
pipenv install Flask flask-cors psycopg2-binary gunicorn requests python-dotenv
```
- PostgreSQL Database Connection
Example of format to place credentials inside a .env file:
```py
DB_USER="___________"
DB_NAME="___________"
DB_PASSWORD="___________"
DB_HOST="___________"
```

---
## Running the app locally using Flask  
**In a terminal:**  
Mac/Linux:  
`FLASK_APP=salty_app flask run`  
Windows:  
`export FLASK_APP=salty_app` (set env var)  
`flask run`



These can be accessed locally at the following addresses: 
```sh 
# /home will return all data in database
http://localhost:5000/
http://localhost:5000/home
http://localhost:5000/top20_saltiest_users
http://localhost:5000/top20_sweetest_users
http://localhost:5000/top10_commenters
http://localhost:5000/top100_salty_comments
http://localhost:5000/top100_sweetest_comments
```  

## Heroku App: https://saltyapp.herokuapp.com/

Endpoints if deployed to Heroku:  
Below are the routes that return key-value pair data in JSON from a postgreSQL database. 
```sh
http://saltyapp.herokuapp.com/
https://saltyapp.herokuapp.com/home
https://saltyapp.herokuapp.com/top20_saltiest_users
https://saltyapp.herokuapp.com/top20_sweetest_users
https://saltyapp.herokuapp.com/top10_commenters
https://saltyapp.herokuapp.com/top100_salty_comments
https://saltyapp.herokuapp.com/top100_sweetest_comments
```
---
## HackerNews API retrieval
To retrieve the comment data from the HackerNews API and populate your database, run `data_grabber.py`


## Database Schema
![](https://i.imgur.com/NEJr8a8.png)

---

## Heroku Deployment
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