# Code2040 Hackday Project

## By Karina, Samuel, Ekua, Fisher, and Miguel.

### Database

We are using Postgres for the database for this project.

- Installing PostgresSQL: You can [download][https://www.postgresql.org/download/] the app or `brew install postgresql`
- Running Postgres: `postgres -D /usr/local/var/postgres`

**Note: If running you are the running the application for the first time, follow this:**
-  Create the database: `createdb hackday`
- Have Django initialize the database: `./manage.py migrate`

Now you can run the app on your local machine

To create a superuser for admin:

`./manage.py createsuperuser`

### Running the application
`./manage.py runserver`

To make new migrations:

`./manage.py makemigrations`

`./manage.py migrate`

To view admin page:

`localhost:8000/admin`

