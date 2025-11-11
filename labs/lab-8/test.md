## Lab #8 - Unit Tests

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
    git checkout -b "lab-8" 
    ```
6. Navigate to your `lab-8` directory
    ```bash
    cd labs/lab-8
    ```

### Lab 
1. Analyze the code provided in `app/app.py`. Understand its functions, queries, and expected behavior.  

2. Identify test cases by brainstorming the different scenarios and edge cases you need to cover with your tests. Consider various inputs, ouputs, and potential errors.

3. Write 5 unit test cases using pytest in `tests/test.py`. I have provided a few examples for you. 

Don't forget to `pip install pytest pytest-flask`

#### 4. Run your tests
From the lab-8 directory, run the command
```bash
python3 -m pytest -v
# or 
python3 -m pytest -s
```

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace. Don't forget to deactivate your virtual environment!

```bash
git add .
git commit -m "completed lab 8"
git push --set-upstream origin lab-8
# or
git push
```