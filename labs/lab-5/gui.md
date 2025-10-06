## Lab #5 - Build an Intentionally Bad GUI

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
5. Create a branch for lab 5
    ```bash
    git checkout -b "lab-5" 
    ```
6. Activate your virtual environment
7. Navigate to your `lab-5` directory
    ```bash
    cd labs/lab-5
    ```

### Lab 
Create an intentionally bad GUI that has:
* at least 3 webpages
* at least 1 navigation method
* at least 1 photo
* at least 1 external style sheet (style.css)

A database is **not** required for this lab. However, I left the DB code in this lab in case you would like
to include a DB to enhance the functionality of your bad GUI. Uncomment lines 24-31 in `app.py` and include 
a `.env` file to initialize your DB.

Keep in mind that:
* webpages are defined in app.py (use index.html as an example)
* images must be stored in the `static` directory
* `style.css` must be stored in the `static` directory

I have gone ahead and created `style.css` for you.

To view the HTML you have written in your browser, run the `app.py` script.

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
* HTML: https://www.w3schools.com/html/
* CSS: https://www.w3schools.com/css/default.asp
* Flask Documentation: https://flask.palletsprojects.com/en/stable/
* Week 6 slide decks

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace. Don't forget to deactivate your virtual environment!

```bash
git add .
git commit -m "completed lab 5"
git push --set-upstream origin lab-5
# or
git push
```

### Extra Credit
Present your awful GUI to the class for 5 extra credit points on your midterm exam.  Add a comment to your brightspace submission to let me know that you will be presenting. **If you would like to present your bad GUI, this lab has to be submitted by 6:30 PM on Thursday, October 9th.**