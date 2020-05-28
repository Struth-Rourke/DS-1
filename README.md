# DS


## Running the app locally using Flask  
**In a terminal:**  
Mac/Linux:  
`FLASK_APP=salty_app flask run`  
Windows:  
`export FLASK_APP=salty_app` (set env var)  
`flask run`



These can be accessed locally at the following addresses: 
```sh 
http://localhost:5000/home
http://localhost:5000/top20_saltiest_users
http://localhost:5000/top20_sweetest_users
http://localhost:5000/top10_commenters
http://localhost:5000/top100_salty_comments
http://localhost:5000/top100_sweetest_comments
```  

## Heroku App: https://saltyapp.herokuapp.com/

Below are the routes that return key-value pair data from a postgreSQL database. 
```sh
https://saltyapp.herokuapp.com/home
https://saltyapp.herokuapp.com/top20_saltiest_users
https://saltyapp.herokuapp.com/top20_sweetest_users
https://saltyapp.herokuapp.com/top10_commenters
https://saltyapp.herokuapp.com/top100_salty_comments
https://saltyapp.herokuapp.com/top100_sweetest_comments
```


