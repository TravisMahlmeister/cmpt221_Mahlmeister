## Lab #10 - Docker

### Pre-Lab
1. Open your `cmpt221` repository in Github and click `sync fork` > `update branch`

2. Open your `cmpt221` repository in VSCode and open your terminal.

3. Pull the changes into main using `git pull --no-edit`

4. Create a new branch for lab 10 using `git checkout -b lab-10`

5. Activate your virtual environment


### Lab 
#### 1. Install Docker Desktop (includes docker engine)
https://docs.docker.com/get-started/get-docker/


#### 2. Follow the step by step instructions in the wk 13 - docker slideshow to
Deploy two containers:
1. postgreSQL container
2. flask container

and create one volume to store database data

# Submission
1. Take a screenshot of your running containers and add it to the labs/lab-10 directory
2. Submit the sign up form and use psql (docker desktop cli or local cli) to view the data stored in the users table. Take a screenshot of the data and add it to the labs/lab-10 directory

```bash
git add .
git commit -m "completed lab 10"
git push --set-upstream origin lab-10
# or
git push
```