## Lab #4 - SQL vs. ORM
### Prerequesites
- Lab 3 must be complete.

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
5. Create a branch for lab 4
    ```bash
    git checkout -b "lab-4" 
    ```
6. Activate your virtual environment from your root directory
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

### Lab - Introduction
Last week, you connected to the `marist` database in `postgres` using `flask` and `sqlalchemy`. This week, you are going to leverage SQL and the sqlalchemy ORM to interact with one of those tables.

**Structured Query Language (SQL)** is a programming language that uses short blocks of code called queries to manage and interact with the data in relational databases.

An **Object Relational Mapping (ORM)** is a programming technique that lets you interact with databases using your programming language’s objects instead of writing sql queries

To connect to your database, copy and paste your `.env` file from your `lab-3` directory into your `lab-4` directory.

```bash
# .env
db_name = marist
db_owner = postgres
db_pass = <your password>
```

### Lab - Part 1
Write SQL queries to accomplish the following in `db/sql.py`:
- Insert 3 records into the Courses table
- Update 1 record in the Courses table
- Delete 1 record in the Courses table

**SQL Resource:** https://www.w3schools.com/sql/default.asp

### Lab - Part 2
Leverage the SQL Alchemy ORM to accomplish the following in `db/orm.py`:
- Insert 3 records into the Professors table
- Update 1 record in the Professors table
- Delete 1 record in the Professors table

After writing the queries, run the `app.py` script.

```bash
python3 app.py
# or
python app.py
```

Then, navigate to your application in your browser and use the buttons provided to run your queries.
All the buttons are doing is navigating to a new Flask `route`. The queries are submitted when we load that page.
That code can be found in `app.py` in the `create_app()` function.

Once the queries are submitted, a select statement will print your table to the console. You will have to refresh the `/sql` or `/orm` page every time you want to submit a query. I recommend taking some time to think about how this same logic can be applied to your group project.

You can also use the PgAmin4 `view/edit data` functionality available for each table to see how your tables have been affected by the queries.

After you have written all of your queries, deactivate your virtual environment.
```bash
deactivate
# or
.venv/Scripts/deactivate.bat
```

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace.

```bash
git add .
git commit -m "completed lab 4"
git push --set-upstream origin lab-4
# or
git push
```