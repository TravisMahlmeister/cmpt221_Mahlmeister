# Lab #1 - Creating a Pull Request

**Pull Request**: A pull request (pr) is a proposal to merge a set of changes from one branch into another. Typically, we see this when we want to merge new code into the main branch. In a pull request, collaboraters can review and discuss the proposed set of changes before the changes are integrated. Pull requests also display the differences between the content in the source branch and the content in the destination branch. If new changes are committed in a branch that has a pull request open, the pull request will be updated with those new changes.

In this class, you will be using pull requests for two things:  
1. Submitting labs
2. Collaboration in your group project

In the README of this repository, there are instructions that explain how to work on and submit a lab in this class. Aside from copying and pasting a link in brightspace, those instructions are simply a guide to creating a pull request. 

This lab is going to walk you through the steps of submitting a lab (i.e. creating a pull request). This way, when it comes time to submit an assignment or create a pull request within your group, you've already been through the process at least once. Consder this lab a practice run.

Before starting this lab, make sure you are in your local repository. You can either open VSCode and select the project, or use the command line shortcut:
```bash
# cd = change directory
# your path may be slightly different depending on where you put your code
cd cmpt221
code .
```

Then, create a new branch in your repository and name it "lab-1":
```bash
# create a new branch and switch to it
git checkout -b "lab-1"
```

Then, verify you are in the new branch:
```bash
# get current branch status
git status
```

Create a new file in the `lab 1` directory and add some content. I don't care what kind of file it is. It can be a `.txt` file, a `.md` file, anything. In the file, write something. Anything. Tell me a joke, a fun fact, or simply write your name. The content doesn't really matter; what we're concerned about is the process. 

When you've finished adding content to your file, you're going to commit and push your changes. When you go to commit your changes, write up a somewhat detailed and/or entertaining commit message explaining what you're committing. Typically, you'll have more than one commit for each lab, but this is a rather small lab, so you only need one.

```bash
# add changes to staging
git add . 
# add a message to your change
git commit -m "your detailed message here"
# send your changes to the repo
git push
 ```

If this is the first time you're pushing to this github account from this machine, you might have to authenticate by signing into Github. You will also need to run the following commands if this is your first time pushing from a new branch. You'll have to run these every time you make your first push from a new branch.  

```bash
# create upstream (remote tracking branch) for your current local branch
git push -u origin lab-1
git push --set-upstream origin lab-1

```

Once you have pushed your new file and you're ready to submit it, go to your `cmpt221` repository and click `Pull requests` in the top menu bar. Click `New pull request`. Make sure your OWN project is selected (not mine) and keep the `base:main`, and select the branch you'd like to compare: `compare:lab-1`. Then click `Create pull request`. Add a title and a description, and click `Create pull request`. 

![Alt text](pr.png)


Once the pull request is created, add `calistaphippen` as a reviewer, copy the link to your pull request, and submit it under `Lab 1` in Brightspace. I will leave comments on your lab in the PR and your lab grade will be available in Brightspace.

This is a change for the class demo. 