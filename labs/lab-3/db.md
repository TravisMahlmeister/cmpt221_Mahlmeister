## Lab #3 - Creating & Connecting to a Postgres DB
### Pre-Lab
1. Open your `cmpt221` repository in Github and click `sync fork` > `update branch`

2. Open your `cmpt221` repository in VSCode and open your terminal. Please refer to README.md for instructions on how to do this. 
3. In your terminal, issue a git switch to switch to the main branch:
    ```bash
    # switch to main branch
    git switch main
    ```
4. Issue a git pull to pull any changes from your remote repository into your local repository
    ```bash
    git pull --no-edit
    ```
5. Create a branch for lab 3
    ```bash
    git checkout -b "lab-3" 
    ```

### Lab - Part 1
In order to connect to a database, you need to _create_ a database. We'll be creating our database in Postgres, so go ahead and download PostgreSQL and pgAdmin4: https://www.postgresql.org/download/

Open the application and follow the set-up instructions. You'll have to set a password for the user `postgres`. **Remember this password.** Once you're set up, you can create your database by following these instructions:

1. Click on the `Servers` dropdown, then the `PostgreSQL 16` dropdown.

2. Right click on `Databases`, click `Create`, then click `Database`

3. Name the database `marist` and leave the owner as `postgres`. Click `Save`

Now that you have a database, you have to connect it to your code. We'll be using `Flask` and `SQLAlchemy` to connect our database. 

`Flask` is a micro web framework. A web framework enables developers to write web applications without having to worry about low-level things (such as protocols). Flask is considered a micro web framework because it doesn't require specific tools and libraries, and doesn't have the features a typical web framework (like django) would have. However, Flask supports extensions, like SQLAlchemy, that can add some of the features that other web frameworks provide inherently.

`SQLAlchemy` is a database toolkit for python. As an object relational mapper (ORM), SQLAlchemy converts python objects into database objects. It also enables developers to insert, manipulate, and delete data in a database by executing SQL from python modules and scripts.

Flask and SQLAlchemy are both python packages that need to be installed with `pip`.

First things first, though... you need to activate your virtual environment.

Navigate to your root directory using the `cd` command if you are not there already. There should be a `.venv` directory in `/cmpt221` (root) from lab-2. If you do not have a virtual environment already created, follow the instructions from lab 2 to create one.

Activate your virtual environment using whatever command worked for you in lab 2 
```bash
# mac
. .venv/bin/activate

# windows
source .venv/Scripts/activate
# or 
.venv/Scripts/activate.bat
# or 
.venv/Scripts/activate.ps1
```

You'll know your virtual environment is activated when you see `(.venv)` in your terminal.
```bash
(.venv) calistaphippen@calistas-mac cmpt221 %
```

I've gone ahead and provided you with the requirements.txt file for this lab. All you need is to run a `pip install`, and all the python packages you need (flask, sqlalchemy, psycopg2, dotenv) will be installed.

```bash
pip install -r requirements.txt
```

**IMPORTANT**: If you run the code in this lab while your virtual environment is not activated, _it will fail_.

To connect to your new database, you'll have to provide the database name, the database owner, and your password. 

We are using the database owner `postgres`, and the database you created earlier is named `marist`.

However, you don't necessarily want this information available for the world to see (especially your password). To hide this information, create a `.env` file.

**A `.env` file is a hidden file used to store configuration settings and environment variables that you don’t want shared/seen in your code.** When you create and use a `.env` file, you have to make sure that `.env` is included in your `.gitignore`. I've already done this for you, but if you want to take a look, check out line 27 in the repo .gitignore file.

Create a new file in the lab-3 directory and name it `.env`. Copy and paste the following code into your .env file, replacing \<your password> with the password you created when you went through the pgAdmin4 set up steps.

```bash
db_name = marist
db_owner = postgres
db_pass = <your password>
```
These values will be substituted into the database connection code after they have imported in by the `dotenv` module.

So, you add your variables to your `.env` file and no one can see them except you. Those variables are then imported into your code using the `dotenv` package, which references the variables by their `key` (think key = value syntax).

Review the code in the `lab-3/db/sever.py` module, but do not change anything. After reviewing the code, run the `app.py` script from the lab-3 directory.  

```bash
python3 app.py
# or
python app.py
```

If you have successfully connected to your database, you will see the following message in your terminal:
```bash
----------- Connection successful!
 * Connected to database: marist
 * Serving Flask app 'db.server'
 * Debug mode: on
``` 

### Lab - Part 2
Once you've established a connection to the database, you can begin creating tables. Since we are using SQLAlchemy, we can create a python class, and SQLAlchemy will convert that class into a table. 

When you ran the application, a `courses` table was created for you. To see it, go into pgAdmin4, click the arrow next to the `marist` database to expand it > `Schemas` > `Tables` > `courses`

Review the code in `lab-3/db/schema/course.py`. Then, using that code as an example, create a class in `lab-3/db/schema/professor.py` that contains columns for a **professor's first name, last name, and email address**. The class has already been started for you.

After creating the class, go to `lab-3/db/server.py` and uncomment line 25. **Then, save your changes.**

Go back to pgAdmin4, right click on `Tables` in the marist database schema, and click `Refresh`. You should now see the `professors` table.

Now, let's think about the relationship between the two tables. For this example, let's assume that professors can teach many classes and that courses are taught by many professors (e.g. there are many professors who can teach SD2).

A many to many relationship means we need to create an association/join table. In flask, there are two methods to accomplish this:
1. Core Table object: Table():  
    Used when only foreign keys will be stored in the table  
2. Association object pattern  
    Used when foreign keys AND additional data will be stored in the table

In this case, we just want the course foreign key and the professor foreign key. We don't want to store any additional information, so we are going with option 1.

The association table has been created for you in `lab-3/db/schema/professorcourse.py`. Go ahead and review it, then uncomment line 27 in `lab-3/db/server.py`. 

**Save your changes**, then, go to pgAdmin4, right click on `Tables` and hit `Refresh`. You should see your association table.

Lastly, right click on the `marist` database and click `ERD for Database`. You should see an ERD containing the three tables you just created.

**Take a screenshot of the ERD and drag & drop it into the lab-3 directory.**

Don't forget to deactivate your virtual environment!
```bash
deactivate
# or
.venv/Scripts/deactivate.bat
```

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace.

```bash
git add .
git commit -m "completed lab 3"
git push --set-upstream origin lab-3
# or
git push
```