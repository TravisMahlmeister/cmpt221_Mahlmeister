## Lab #6 - Login

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
5. Create a branch for lab 6
    ```bash
    git checkout -b "lab-6" 
    ```

6. Navigate to your `lab-6` directory
    ```bash
    cd labs/lab-6
    ```

7. Activate your virtual environment
9. Create a .env file to connect to the `marist` database.

### Lab 
Create a login form that requires a user's email and password.
* if the password matches, route the user to the success page
* if the password doesn't match, route the user to the login page (We will cover validation in the next lab)

Keep in mind that:
* webpages are defined in app.py (use index.html as an example)
* you need to pull the user's email and password from the database
* you need to compare the user's email and password from the databse to the input values

To view the HTML, run the `app.py` script.

```bash
python3 app.py
# or
python app.py
```

and click on 
```
 * Running on http://127.0.0.1:5000
```
_**Note:** If app.py is not running, you will not be able to view your webpages._  
_**Note:** Don't forget to refresh your web broswer to apply HTML/CSS changes._

**Helpful References:**
* Flask forms: https://testdriven.io/courses/learn-flask/forms/
* Week 3, 4, 5, 6, 8 slide decks

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace. Don't forget to deactivate your virtual environment!

```bash
git add .
git commit -m "completed lab 6"
git push --set-upstream origin lab-6
# or
git push
```