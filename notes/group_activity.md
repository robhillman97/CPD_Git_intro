# Group Activity

While git is great for helping you keep a backup of your code online, this is only a fraction of what it offers.  Where git starts to shine is when you start working in a team on the same code.  To highlight this, we will be working as a team for the next activity.

## The Goal

I want everyone to add a short "hello world" program into the `code` folder of this repository (preferably in Python, but the language does not matter too much).  During this exercise I want everyone to also practice *reviewing* another classmate's submitted code.

### Note
I will need everyone to come up and have their GitHub account added to the shared repository.  Once added, everyone can clone the repository to their local computer.

## Good coding practices
Whether you are working alone or working in a team, one of the most valuable things you should keep in mind is **context transfer**.  It is not enough to just track the changes made to the code, but to also track **why** those changes were made.  Many of the best practices covered within this lecture will be various flavors of recoding this kind of context in a way that is clear to other developers, or even to yourself when you look back at old code.

When context is well recorded it becomes easier for other develops to be on-boarded into your codebase, structural changes to the code become easier to manage, and overall it leads to code that is easier to maintain in the long run.

### Context transfer

Ways to boost context transfer:

- Pair programming: Work with another developer in real time when writing your code.  Typically you have one person drive the keyboard focusing on code syntax and code legibility while the other drives the code structure focusing on how the code should be organized and the algorithms being used.  It is typically useful to switch these roles every so often.
- Git commit messages: Include the **why** for every change directly in the commit message
- GitHub Pull Requests: Use this space for the larger reason behind any changes and/or features
- [Architecture Decision Record](https://github.com/joelparkerhenderson/architecture-decision-record) (ADR): For larger code bases ADRs can be used to track changes to a code's architecture over time.  These records are kept in the repository next to the code and can be refereed to by any developer who wants to know why the code is structured the way it is. 

## The Instructions

There are many different ways to effectively use git within a team, and many more ways to have it be a nightmare.  For this lecture we will be using the workflow I use when working with the Zooniverse.  The workflow is as follows:

1. checkout the `main` branch and pull down the latest changes
2. make a new branch with a descriptive name
    - for better organization of branch names you can prepend branch names with `feature/`, `bug/`, `hotfix/`
3. write your code grouping logical units of changes into individual commits
4. push the changes to the common remote repository and open a `Pull Request` (PR) on GitHub
5. assign a reviewer for your PR (it is your job to ask someone to look at your code, don't expect the PR to "just be seen" by other developers)
6. address any feedback left by the reviewer
7. once approved **rebase** your changes onto the latest `main` branch to ensure there are no code conflicts
or if you want to clean up your git history rebase in interactive mode (`git rebase -i main`)
    - Often this can be done with a button on GitHub
8. push the rebased code back to the remote
9. merge to the `main` branch using the big green button
10. delete the branch on the remote once the merge is finish
11. pull the latest `main` (with your PR merged) locally
12. (optional) delete your local copy of the merged branch

### **Note**
After the rebase when you go to push back to the remote (step 8) you may need to use `--force-with-lease` switch.  This is needed if any of the git history is re-written during the rebase.  This switch is a slightly safer version of `--force` where it will only let you continue if you are not overwriting the work of a different developer on the same branch.  This prevents you from accidentally deleting someone else's work.

And these steps in code:
```bash
# get latest code on main branch
git checkout main
git pull

# make new working branch
git checkout -b feature/my-feature-branch
git add my_new_file.py
git commit
git push --set-upstream origin feature/my-feature-branch
# make PR on GitHub

# get latest changes to main and rebase
git checkout main
git pull
git checkout feature/my-feature-branch
git rebase main
git push --force-with-lease origin feature/my-feature-branch

# after merge on GitHub update your main branch
git checkout main
git pull

# clean up
git branch -d feature/my-feature-branch
```

What does this workflow achieve?
- It ensures only reviewed code makes it into the `main` branch
    - This implies the `main` branch will always have working code
- It encourages short lived feature branches
    - Smaller code changes are easier to review and less likely to conflict with other developers' code changes
- As the code writer you are responsible for addressing merge conflicts
- By using `rebase` rather than `merge` the git history is kept linear
    - This makes it easier to find when a particular change happened and any context that was left in commit messages
- Once given the OK by the reviewer the code writer makes the final decision on when to merge
- Any merged branch can be safely deleted, there is no need to clutter up the remote with old branches (also you are less likely to have multiple developers pick the same branch name for their work if there are fewer branches on the remote repo).

### **Note**
With this workflow, every developer is working on **different** branches.  If multiple people are working on a single feature they should create a branch for the feature, and **each** branch off of that new feature branch.  They can both make PRs into/rebase onto the feature branch.  Once the feature is done a new PR that brings it into the `main` branch should be made.  As everyone is on a independent branch merge conflicts only happen at the rebase stages, rather than on pulls or pushes.


## Writing better commit messages

This section of notes is partially adapted from gov.uk's style guides found at:

- [https://github.com/alphagov/styleguides/blob/master/git.md](https://github.com/alphagov/styleguides/blob/master/git.md)

As mentioned in the previous section, context transfer is the main goal for writing easy to maintain software.  Writing good commit messages is one way to do this.  Here is an example of a good commit message:

```
Write better commit messages

The first line says what the commit does and should be kept under 50
characters, a blank line is inserted after it.  The full context of the
commit is expanded on in any text that comes after.  Use this space to
talk about the **why** of the code change and any consequences the
changes might have.

Depending on the group you are working in, you might be required to hard
wrap your longer context at 72 characters to make the messages more
readable when shown on the terminal with the `git log` command.

When making a new PR on GitHub for a branch that only has one commit the
first line of the commit will be used as the default title of the PR and
the longer message used as the PR's default text.  If you are hard
wrapping lines your PR's text will also be hard wrapped in the browser's
text input box.  You may need to reformat it before opening the PR.

If you are fixing an issue reported on GitHub include the issue number
in the message as:

- close #XXX
- closes #XXX
- closed #XXX
- fix #XXX
- fixes #XXX
- fixed #XXX
- resolve #XXX
- resolves #XXX
- resolved #XXX

GitHub will automatically close the mentioned issue once the PR is
merged into the repo's **default** branch.
```

## Writing better PRs

This section of notes is partially adapted from gov.uk's style guides found at:

- [https://github.com/alphagov/styleguides/blob/master/pull-requests.md](https://github.com/alphagov/styleguides/blob/master/pull-requests.md)

Once you have a branch with some commits you want to merge into the main branch, the next step is to have those changes reviewed by another developer.  On GitHub this process is known as creating a Pull Request (PR).  When opening a PR you should provide a detailed description of changes introduced, the reason the changes were made, and any specific things the reviewer should be aware of when testing your code.  If the PR is in reference to an open issue on the repo this should be mentioned as well.

## Writing better code reviews

When working in a team it is important to review other people's code along side writing your own code.  While it might be tempting to just quickly look code changes on GitHub and leave a short message like "looks good to me" that is only useful for very small changes to the code.  For larger changes a full review should be done.

1. Pull down the changes locally
```bash
git checkout main
git pull  # also fetches the names of all remote branches
git checkout <name of branch on remote>
# or in newer versions of git
git switch <name of branch on remote>
```
2. Read the PR to see what changes were made
3. Test that those changes work as intended
    - Use the code that was changed.  If you don't know how, ask for an example use case on the PR
4. If the PR is fixing a bug:
    - Reproduce the bug on `main`
    - Switch to the PRs branch and ensure the bug is fixed
5. Look over the code diff on GitHub and leave inline comments
    - Questions about how code works
    - Suggestions for make the code easier to read and/or more efficient
6. Write your review (GitHub supports full markdown, don't be afraid to use section headings and lists in your review)
    - Open with a summary of the changes made, this allows the person who opened the PR to see if you understood the changes correctly
    - List the steps you took to test the code
    - Record any observations you made during the testing process
    - If appropriate list any consequences of the changes (e.g. is there other code that should be changed in a future PR as a result)
    - Any actions the PRs author(s) should take before merging
7. Either approve or block (pending changes) the PR
8. If approved you are done, it is the responsibility of the author(s) to merge the PR.  If not, re-review when the changes you asked for are finished.

Here is an example of well constructed PR and review taken from one of the Zooniverse's repositories [https://github.com/zooniverse/front-end-monorepo/pull/2313](https://github.com/zooniverse/front-end-monorepo/pull/2313).
