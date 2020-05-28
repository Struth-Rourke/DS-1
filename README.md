# DS

## Resources
- Postgres Database
- VADER Sentinment Analysis
- Flask
- Heroku  

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