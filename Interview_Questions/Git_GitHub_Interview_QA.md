## -----------DAY 05----------3/Aug/'26-----------------
1. What is Git?
        `Git is a distributed version control system.
        `It tracks the changes made to the source code, and stores them as different versions(maintains a history of changes). 
        `It helps developers to preserve the previous versions(changes) of the code and collaborate on the same project, simultaneously.
        `Unlike centralized systems, Git allows developers to work offline as each developer has the source code(or the repository).
    ## Key points:
        - Distributed version control system
        - Tracks changes
        - Maintains version history
        - Supports collaboration
        - Enables offline work
    ## Real-world Example:
        Imagine three developers are working on the same project.
        Git allows each developer to make changes independently, save them as commits, and later combine those changes without losing previous versions.
---------------------------------------------
2. What is GitHub?
        `GitHub is a cloud-based platform that hosts Git repositories.
        `It allows developers to store their code remotely, collaborate on projects, and manage version-controlled repositories using Git.
    ##  Key Points
        - Cloud-based platform
        - Hosts Git repositories
        - Remote code storage
        - Collaboration
        - Uses Git for version control
---------------------------------------------
3. What is the difference between Git and GitHub?
        `Git is a distributed version control system, whereas GitHub is a cloud-based platform that hosts Git repositories.
        'Git is the version control tool used to track and manage changes in source code, while GitHub provides remote storage and enables developers to collaborate on Git repositories.
        'GitHub uses Git to maintain version-controlled repositories.
    ### Key Points
        - Git → Version control tool
        - GitHub → Cloud-based hosting platform
        - Remote repository hosting
        - Collaboration
        - GitHub uses Git
---------------------------------------------------
4. What is a Git commit? What is the purpose of a Git commit?
        'A Git commit is a snapshot of the changes made to a Git repository at a particular point in time.
        `The purpose of a commit is to save and record changes, making it easier to track the project's history
        `Each commit contains:
                - The changes made to the files
                - A meaningful commit message
                - Author information
                - Date and time of the commit
                - A unique commit ID (hash)
    ### Syntax
        git commit -m "Meaningful_Message"    
    ### Key Points:
        -Snapshot of changes
        -Records project history
        -Restore previous versions
        -Collaboration
        -Commit message
        -Unique commit ID (Hash)
----------------------------------------------------
5. Why do recruiters like to see a GitHub profile?
        `Recruiters like to see a GitHub profile because it showcases a candidate's coding skills, consistency, and practical experience. 
        `It allows them to review projects, code quality, problem-solving ability, and contribution history, giving them confidence in the candidate's technical abilities beyond what's written on a resume.
    ## Key Points
        -Demonstrates coding skills
        -Shows practical projects
        -Reflects consistency (commit history)
        -Highlights code quality
        -Shows problem-solving ability
        -Supports the resume with real work
-----------------------------------------------------------------
6. What is a Git repository?
    ### Definition :
        A **Git repository (repo)** is a storage location where Git tracks and manages all the files, folders, and the complete history of changes made to a project.
        It stores:
            - Source code
            - Project files
            - Commit history
            - Branches
            - Version history
    ### Types of Repository
        **1. Local Repository**
            - Stored on your computer.
            - Used for developing and committing changes.
        **2. Remote Repository**
            - Stored on a remote server (e.g., GitHub).
            - Used for backup, collaboration, and sharing code.
    ### Example:
        When you run: git init
                    Git creates a hidden **`.git`** folder inside your project.
                        My_Project/
                        │
                        ├── main.py
                        ├── README.md
                        └── .git/
                    The `.git` folder stores:
                        - Commit history
                        - Branch information
                        - Configuration
                        - Version history

    ### Common Interview Follow-up
       **Can you see the `.git` folder?**
        Yes. It is a **hidden folder**. It contains all the information Git needs to track your project.
    ### Easy Trick to Remember : **Repository = Project Folder + Git History**
                 Think of it as: **Repository = Files + Version History**

-----------------------------------------------------------------

7. What is the difference between git fetch and git pull?
    # Fetch
        Git Fetch downloads the latest changes from the remote repository without merging them into the local branch. This allows developers to review the latest changes while keeping their local code unchanged.
        ## Syntax:
            git fetch origin <branch_name> 
    # Pull
        Git Pull downloads the latest changes from the remote repository and automatically merges them into the current local branch.
        ## Syntax:
            git pull origin <branch_name>    
    #### ==>   git pull = git fetch + git merge
    ## Key Points
        Git Fetch :
            Downloads latest changes
            No automatic merge
            Safe to review changes first
        Git Pull :
            Downloads latest changes
            Automatically merges changes
            Updates the local branch   
----------------------------------------------------------
8. Explain the Git workflow (add → commit → push).
        The Git workflow consists of three main steps:
    **1. ADD**
        -Moves the changes from the **Working Directory** to the **Staging Area**.
        -It selects the files that should be included in the next commit.
        -Syntax:  git add .
                    OR
                git add <filename>
    **2. COMMIT**
        -Saves the staged changes as a snapshot in the **Local Repository** along with a meaningful commit message.
        -Syntax:  git commit -m "Meaningful_Message"
    **3. PUSH**
        Uploads the committed changes from the **Local Repository** to the **Remote Repository** (e.g., GitHub).
        -Syntax:  git push origin <branch_name>

                            * WORKING DIRECTORY
                                    │
                                 git add
                                    ▼
                            *  STAGING AREA
                                    │
                                git commit
                                    ▼
                           * LOCAL REPOSITORY
                                    │
                                git push
                                    ▼
                       * REMOTE REPOSITORY (GitHub)


## ===============QUICK REVISION=================================
- Git          → Version Control
- GitHub       → Remote Repository Hosting
- Repository   → Project folder
- `git add`    → Working → Staging
- `git commit` → Staging → Local Repo
- `git push`   → Local → GitHub
- `git fetch`  → Download only
- `git pull`   → Download + Merge
- `clone`      → Local copy
- `fork`       → GitHub copy
## ================================================================