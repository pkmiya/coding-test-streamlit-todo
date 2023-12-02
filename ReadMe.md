# *Table of Contents*
- [*Table of Contents*](#table-of-contents)
- [Setup](#setup)
  - [Database](#database)
    - [Install PostgreSQL](#install-postgresql)
    - [Create a database](#create-a-database)
  - [Common](#common)
  - [Backend](#backend)
- [Run](#run)
  - [Backend](#backend-1)
  - [Frontend](#frontend)
- [Other](#other)
    - [Chore](#chore)


# Setup

## Database

### Install PostgreSQL

- Type `sudo apt install postgresql` to install PostgreSQL
- Type `passwd postgres` to set the password for the default user `postgres`
- Type `su - postgres` to change to the user `postgres`
  (Type `psql -d postgres` to enter the PostgreSQL shell)
- Type `sudo service postgresql start` to start the database server
- Change these 2 conf files
  - About the filename
    - The path varies depending on the version of PostgreSQL
    - Type `psql --version` to check the version
    - Change the path accordingly
  - `sudo vim /etc/postgresql/14/main/postgresql.conf`
    - Change `#listen_addresses = 'localhost'` to `listen_addresses = '*'`
  - `sudo vim /etc/postgresql/14/main/pg_hba.conf`
    - Change like below:
    ```
    # IPv4 local connections:
      #host    all             all             127.0.0.1/32            md5
      host    all             all             0.0.0.0/0               md5
    ```
- Type `sudo service postgresql restart` to restart the database server

### Create a database

- Type `CREATE DATABASE streamlit_todo;` to create a database named `streamlit_todo` (this name is used in `.env` file)
- Type `\c streamlit_todo` to connect to the database
- Type the following commands to create tables
  ```SQL
  CREATE TABLE todo_list
  (
    id serial PRIMARY KEY,
    deadline date,
    todo character varying,
    priority integer,
    genre character varying,
    is_done character varying,
    created_at date
  );
  ```
  - If necessary,
    - Type `ALTER TABLE table_old RENAME TO table_new;` to change the table name
    - Type `ALTER TABLE todo_list RENAME COLUMN col_old TO col_new;` to change the column name
    - Type `DROP TABLE todo_list;` to drop the table
    - Type `DROP DATABASE streamlit_todo;` to drop the database

## Common

- Type `pip install -p requirements.txt` to install pip dependencies
  - If packages are downloaded in user path (like `/home/pkmiya/.local/bin`), add PATH via
    ```shell
    PATH=$PATH:/home/pkmiya/.local/bin' >> ~/.bashrc
    source ~/.bashrc
    ```

## Backend

- Install necessary packages

  - Type `sudo apt install uvicorn` to install uvicorn
  - Type `pip install -r requirements.txt` to install pip dependencies

- Set environment variables
  - Type `.env.example` by `cp .env.example .env` to create a `.env` file based on `.env.example`
  - In `.env` file, enter database credentials

# Run

## Backend

- Start the database server
  - Type `sudo serivce postgresql status` to check the server status
  - If the server is not running (it displays `14/main (port 5432): down`), start it via `sudo service postgresql start`
- Start the API server
  - Type `uvicorn main:app --reload` to start the backend server
- Go to http://127.0.0.1:8000/docs in your browser to view the API documentation
  - The document is based on Swagger UI (OpenAPI 3.0)

## Frontend

- Type `streamlit run front.py` to start the frontend server

# Other
### Chore
- Type `find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf` to remove cache files