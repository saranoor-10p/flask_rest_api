# flask_rest_api
This flask rest api perform CURD operation in postgresql database.

# Install and Run Project

1. Install postgres on your local computer
2. Create a database called "" as your local database 
     
    - `sudo su - postgre`

    - `psql`
    
    - `create database wordcount_dev;`

    - `\q`

3. configure database in flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<paaword>@localhost:5432/<database-name>'

4. Run python main.py with `db.create_all()` 

5. Run unit tests

