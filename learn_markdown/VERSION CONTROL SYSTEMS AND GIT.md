
# Task: Research version control and intro to Git

## Version Control System

### What is a VCS?
A software tool that helps manage chanes to their codebase over time. 
It allows you to:
* Track changes
* Revert to past versions
* Collaborate with multiple people
* Manage different project versions

### When to use a VCS?
Whenever you want to do any of the above four things, but essentially:
when you are working collaboratively and want to have snapshots of your 
software development that you can roll back to.

## Types of Version Control

### What is manual version control?
This is when developers manually track and manage changes to their
codebase. They might do this through:
* simple numbering
* date-based numbering
* date-based naming
* backup directories
### What are challenges to manual version control?
* error-prone
* inefficient and time consuming
* not designed for easy collaboration
* lack of history

### How did early version control systems work?
1. Local version control:
* Source Code Control System (SCCS) stored deltas (the differences
* between versions). Only one person can edit at a time.
* Revision Control System (RCS) added branches and tag functionalities.
2. Centralised Version Control:
* Concurrent Version Systems (CVS) created a central repo where all
versions of the files were stored. However, multiple users had to coordinate
their work to avoid conflicts. 
* Subversion introduced atomic commits, directory versioning and 
better conflict resolution.

### Centralised VCS vs Distributed VCS like Git

#### Centralised VCS:

- Single source of Truth
- Client-Server model
- easier to manage/understand
- easier to control access permissions
- suitable for smaller teams with simpler workflows
- single point of failure
- need constant network connection
- slower performance for large projects

#### Distributed VCS:

- Each developer has a complete copy of the repo on their machine.
- Changes are commited locally and then pushed to remote repos ("decentralised")
- Faster performance and offline work
- Improved collaboration
- Improved robustness as not relying on a single server
- More complex to learn and manage
- suitable for large teams

![CVCS-vs-DVCS.png](../images/CVCS-vs-DVCS.png)

## Local Version Control with Git

#### What is stored in each version of a file that changes?

- Diff / delta
- Metadata (timestamp, author, commit message, parent commit)

#### Does Git need to be used as a distributed VCS?

No, you can run it on a server. It may limit the ability to work offline and
its robustness, however.

#### What does Git store in a 'commit'?

A snapshot comprising:
- A reference to a tree object
- Metadata (author, committer, timestamp, commit message, parent commits) 

#### What are the three states in Git?

1. Modified: This means you've changed the file, but you haven't yet told Git that you want to save a snapshot of those changes.   
2. Staged: This means you've marked a modified file in its current version to go into your next commit snapshot.   
3. Committed: This means that the data is safely stored in your local database.

#### Where does Git store its information?

Answer: in a hidden .git directory at the root of your project directory, containing:
- Ojbects
- Refs
- HEAD (this file points to the currently checked-out commit)
- Config
- Index (the staging area)

#### What is the common workflow of git commands?

1. Clone the Repository:
__git clone <repository_url>__
This creates a local copy of the remote repository on your machine.
2. Create a New Branch:
__git checkout -b <branch_name>__
This creates a new branch for your feature or bug fix.
3. Make Changes:
Edit files in your working directory.
4. Stage Changes:
__git add <file_name> or git add .__
This stages the changes to be included in the next commit.
5. Commit Changes:
git commit -m "Commit message"
This creates a snapshot of the staged changes and saves it to the local repository.
6. Push Changes:
__git push origin <branch_name>__
This pushes your local branch to the remote repository.
7. Pull Changes:
__git pull origin <branch_name>__
This fetches changes from the remote repository and merges them into your local branch.   
Additional Common Commands:

__git status__: Shows the current state of your working directory.
__git diff__: Shows the differences between the current version and the previous version of a file.
__git log__: Shows the commit history.
__git branch__: Lists all branches in the repository.
__git checkout <branch_name>__: Switches to a different branch.
__git merge <branch_name>__: Merges the specified branch into the current branch.
__git reset --hard HEAD^__: Resets the current HEAD to the previous commit.
This is a basic workflow, and there are many variations and more advanced techniques that can be used depending on your specific needs.