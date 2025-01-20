# Git and Git-Hub
At some point in your research you will likely have a massive hard drive crash, or realize you introduced a bug in your code and want to revert it back to its working state (perhaps from several weeks before).  Or you may end up working on a bit of code with other people.  In any of these cases version control saves the day.  This document with give you an introduction to `Git` and [`Git-Hub`](https://github.com/) as a version control solution.

## Before you start
+ Install `git`: https://git-scm.com/downloads
+ Create a `Git-Hub` account: https://github.com/
+ Set up ssh key with `Git-Hub` account: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent (optional)
+ Set up Two-Factor Authentication for `Git-Hub`: https://help.github.com/articles/about-two-factor-authentication/ (optional)

## Useful documentation
+ The Git Book: https://git-scm.com/book/en/v2

## Making a repo on Git-Hub
When you click on the "New repository" button on Git-Hub you will see the following:

![Git-Hub new repo](git-hub_new_repo.png)

Here you can enter in some information about your repo:

+ Repository name: the name of you repo and this will also be in the url for the repo
+ Description: Some test to start off your README file
+ Public/Private repo: public repos are free, as a student private ones are too (see https://education.github.com/pack)
+ Initalize README: If checked this will place a README.md file in your new repo.  The README is a [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) file that is displayed on the repo's home page.
+ Add .gitignore: A `.gitignore` file tells git what files to ignore in a repo (e.g. `.pyc` files), there are useful templates for several languages you can start with.  If you are coding in python I would suggest picking it from the dropdown list.
+ Add a license: **Do this!**  You should always add a license to you code, if you are unsure what license to use click the `i` button and read up on the different types (http://choosealicense.com/).  I would recommend either the `MIT` or `Apache 2.0` license for your work.

### Clone a local copy
Now that you have a new repo online it is time to get a local copy on your computer.  Open a terminal and `cd` to the directory you want your repo to live.  On Git-Hub click the "Clone or download" button, if you set up an ssh key click the "Use SSH" link, if you did not, make sure you use the "Use HTTPS" link.  Here is an example of an ssh link:

![Git-Hub clone via ssh](git-hub_clone_repo.png)

Copy the link provided and go back to your terminal and type the command:
```bash
git clone <link you copied>
```

## Making a local repo
You can also make an existing folder into a git repo.  If you plan to keep back ups of this code on Git-Hub (like you should), start by making a blank repo on Git-Hub (see above) and just give it a name.  Once you do that you will see the following:

![Git-Hub blank repo](git-hub_blank_repo.png)

This gives you the step-by-step code for initializing your repo and setting the `remote` URL correctly.  Again, if you have `ssh` set up make sure you have the "SSH" button pressed, and if you don't make sure the "HTTPS" button is pressed.

### Git without Git-Hub
You can also just use git without pushing your code up to Git-Hub.  To initialize git in a directory:
```bash
cd <dirctory>
git init
```

# Git setup
Before we start using git there are some basic configuration:
```bash
git config --global user.name "<your name>"
git config --global user.email <your email>
git config --global core.editor <your text editor (defaults to vim)>
```

Check that your configuration look correct:
```bash
git config --list
```

## Note: 
If you want to use `nano` as the default editor you can do that with:
```bash
git config --global core.editor "nano"
```

If you want to use `vscode` as the default editor you can do that with:
```bash
git config --global core.editor "code -n --wait"
```

## getting help
If you ever need help with a git command:
```bash
git help <command>
git <command> --help
```

# Git basics
Now that you have your repo set up it is time to learn how to use version control.  The basic workflow for `git` is: add/make changes to a file, stage files for a commit, commit the files to the repo, push commits to remote server (e.g. Git-Hub).

## checking the status of your repo
At any time you check the status of your repo (i.e. what files have changed, and what files are staged for commit) with:
```bash
git status
```
This screen helpfully tells you how to "undo" staged files (more on this below).

## staging files for a commit
You can stage changes for a commit by using the `add` command:
```bash
git add <file>
```
Or a if you want to add all files that have changed:
```bash
git add .
```
To unstage a file that was _never_ committed before (keeps local changes):
```bash
git rm --cached <file>
```
To unstage a file that was committed before (keeps local changes):
```bash
git reset HEAD <file>
```
To undo changes made to a file (revert it back to previous commit):
```bash
git checkout -- <file>
```


## commiting changes to a repo
After files are staged you can commit the changes using:
```bash
git commit
```
This will open a text editor for you to type a commit message into.  This should be a short description of what things were changed in the commit.  If your commit message is short you can also use:
```bash
git commit -m "<your commit message here>"
```
**Note** Once a commit has been made that version of the file will _always_ be in your repo.  You will always be able to return to this version of the code (this is the point of version control).  Because of this **_never_** commit sensitive information (e.g. passwords, private data, etc...) to a public repository.

## pushing changes to Git-Hub
If you have your remote repository set up (see above), you can push your commits with:
```bash
git push
```

## pulling changes from Git-Hub
If you are working on several computers, or you are working with other people, you can pull changes down from the remote repository with:
```bash
git pull
```

## code conflicts
If your local version of the code conflicts with the remote version of the code (e.g. the same file was edited) you will not be able to `push` or `pull` the code without resolving the conflicts.  Git will indicate were the conflicts are in the code with blocks that look like:
```
<<<<<<< HEAD
nine
=======
eight
>>>>>>> branch-a
```
Edit this block to look like the version you want, than stage the file with `git add`.  You can see where the conflicts are with `git status`.  Once all conflicts are resolved `git commit` your changes.

# Branches (and why you should use them!)
Git lets you keep several versions of you code at once via a branch system.  A good habbit to get into is to only use the `main` branch (the default first branch) for working/finished code, and use branches to test out new features.  Once the new feature is finished then it's branch is merged into the `main` branch.  

This is very useful if multiple people are working on the same code.  Each person works in their own branch, and when they are done they update their `main` branch to pull in the work of others, than merger their own work into `main` (and deal with any merge conflicts).

## list all your branches
```bash
git branch
```

## switch to a new branch
```bash
git checkout <branch name>
```

## to make a new branch (and switch to it)
```bash
git checkout -b <new branch name>
```

**Note** Any uncommitted changes are carried over when you make a new branch.  So if you started editing your `main` branch by mistake you can just make a new branch and not loose any of the changes you made or mess up your `main` branch.

## merging a branch
```bash
git checkout main
git merge <branch name>
```
If there are any conflicts during the merge resolve them as stated above.

**Note** In this example we are merging the branch into `main`, but `main` is just a branch like any other (there is nothing special about `main`).  You can merger any two branches.
