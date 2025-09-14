## Lab #2 - Pip & Virtual Environments
### Pre-Lab
**IMPORTANT:** To complete this lab, Windows users will need to install Python if it is not already installed: https://www.python.org/downloads/

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
5. Create a branch for lab 2
    ```bash
    git checkout -b "lab-2" 
    ```

### Lab
**PIP**: Pip is installed with Python and enables us to install packages in our programs that aren't already included with Python by default. When you install packages with Pip, they're installed _globally_, which means they are available to all the projects you create _on your computer_.

First things first, let's prove you have pip installed by listing all the packages you have installed on your computer.

```bash
# list pip packages
python3 -m pip list
# or
pip list
```

This command outputs a list of all packages installed on your computer by pip and which version each package is.

Cool. But you may be thinking: what happens when different projects need the same package with different versions?

A **Virtual Environment** is an isolated workspace that allows us to keep dependenceies required by different projects separate. _What?_

It's not uncommon for you to have multiple Python projects on your computer, and sometimes those projects have different requirements. 

When you did a `pip list`, you saw versions next to each package. Different projects might require different versions of the same package. This is where virtual environments come in. When you create a virtual environment, you can install the version of a package you need for one project, and _your other projects won't be affected_. This is because your _scope_ has changed. You are now only installing packages _local_ to your virtual environment. Any projects inside the virtual environment will be affected, while those outside the virtual environment will not be affected. 

You run virtual environments locally (on your own computer), and you don't push them to Github or include them in your final deliverable.

So, let's create one.

First, install `virtualenv` using pip:

```bash
# install virtualenv
python3 -m pip install virtualenv
# if you have issues with the above command, 
# install virtualenv as sudo, to avoid $PATH issues
python3 -m pip install --user virtualenv
```

**IMPORTANT:** You need to be in the root directory (cmpt221) because that is where we want to virtual environment to be created. In your terminal, issue the `pwd` command to verify you're in the right directory.
```bash
# confirm directory
pwd
```

Create a virtual environment named .venv. This command creates a directory named `.venv` which is your virtual environment. Note that you can technically name your virtual environment whatever you want, just make sure to add it to your gitignore file.
```bash
# create venv
virtualenv .venv
# or use this command if you get a command not found error
python3 -m virtualenv .venv
```

Notice the period before the word `venv`? This means the directory is hidden. You can view it with the `ls -a` command. If you click the drop down arrow next to the `.venv` directory icon in your side bar, and then click `bin` (or `Scripts` if you are on windows), you will see an `activate` script. We will call this script to activate our virtual environment.
```bash
# activate venv
# mac
. .venv/bin/activate

# windows
# note: if a command doesn't work, try the next one
source .venv/Scripts/activate
# or 
.venv/Scripts/activate.bat
# or (works in powershell - switch to powershell instead of bash
.venv/Scripts/activate.ps1
```
Once you have activated your virtual environment, you should see a (.venv) in your command line like so:
```bash
(.venv) calistaphippen@calistas-mac cmpt221 % 
```


install the following packages using pip:

```bash
# flask package
python3 -m pip install flask
# or
pip install flask
 
# sqlalchemy package (sql wrapper)
python3 -m pip install flask-sqlalchemy
# or
pip install flask-sqlalchemy

```

Then issue a `pip list` and make sure you see your newly installed packages in the list. 

```bash
# list pip packages
python3 -m pip list
# or
pip list
```

To share your virtual environment (and submit this lab for a grade), make sure you are still in the cmpt221 root directory and issue a `pip freeze`. If you are not in the right directory, you will export all of your installed packages, not just the ones in your virtual environment.
```bash
# store venv configurations
pip freeze > requirements.txt
```

A `requirements.txt` file is simply a list of the modules and packages that your project needs to run. when you recieve a requirements.txt from others (this will be important as you will be working in groups) you can add those requirements to your virtual environment with a `pip install`.

**IMPORTANT**: Do **NOT** run this command for this lab. You _will_ need to run it for your group project.
```
pip install -r requirements.txt
```

Deactivate the virtual environment using the `deactivate` command, then issue another `pip list`. What do you notice?
```bash
# deactivate venv
deactivate
# or
.venv/Scripts/deactivate.bat
```
If all has gone well, you should notice that upon deactivating your virtual environment, you no longer see the packages you just installed.

Once you have completed this lab, push your work to Github. Note: Your `.venv` directory will not be pushed to git because of our `.gitignore`, but your `requirements.txt` file will be.
```bash
git add .
git commit -m "completed lab 2"
git push --set-upstream origin lab-2
# or
git push
```

Then, open a pull request, assign me as a reviewer, and copy/paste the link to the pull request in Brightspace. I will leave comments on your lab in the PR and your lab grade will be available in brightspace.