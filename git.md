# 🧠 Git Cheatsheet

## 📦 Basic Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 🚀 Starting a Project

```bash
git init                # Initialize a new Git repo
git clone <url>         # Clone an existing repo
```

## 📄 Basic Workflow

```bash
git status              # Show changed files
git add <file>          # Stage a file
git add .               # Stage all changes
git commit -m "Message" # Commit with a message
```

## 🔄 Working with Remote

```bash
git remote -v                     # Show remotes
git remote add origin <url>      # Add remote repo
git push -u origin main          # Push first commit
git push                         # Push changes
git pull                         # Pull latest changes
```

## 🌿 Branching

```bash
git branch                       # List branches
git branch <branch>              # Create new branch
git checkout <branch>            # Switch to branch
git checkout -b <branch>         # Create + switch
git merge <branch>               # Merge branch into current
```

## 🔍 Viewing History

```bash
git log                          # Commit history
git log --oneline                # Condensed log
git diff                         # View unstaged changes
git diff --staged                # View staged changes
```

## 🧹 Undoing Changes

```bash
git restore <file>               # Discard changes in working dir
git restore --staged <file>      # Unstage file
git reset HEAD~                  # Undo last commit (keep changes)
git reset --hard HEAD~           # Undo last commit (delete changes)
```

## 🐛 Stashing Work

```bash
git stash                        # Save work in progress
git stash apply                  # Re-apply last stash
git stash list                   # List stashes
git stash pop                    # Apply and remove from stash
```

## 🔐 Tags

```bash
git tag                          # List tags
git tag <tagname>                # Create tag
git tag -a <tagname> -m "msg"    # Annotated tag
git push origin <tagname>        # Push tag
```

## 🧪 Useful Commands

```bash
git show <commit>                # Show details about a commit
git blame <file>                 # Show who changed each line
git clean -fd                    # Remove untracked files/directories
```

## 🧠 Tips

- `.gitignore` — List of files/folders to ignore.
- `HEAD` — Refers to current commit/branch.
- Always pull before you push to avoid conflicts.
- 
```bash
#Ignore the entire "logs" folder
logs/

#Ignore "build" folder at repo root
/build/
