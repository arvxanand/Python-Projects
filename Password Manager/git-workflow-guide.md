# Git Workflow Guide for Python Projects
*A complete reference from your learning journey*

---

## Table of Contents
1. [Basic Concepts](#basic-concepts)
2. [Feature Branch Workflow](#feature-branch-workflow)
3. [Common Commands Cheat Sheet](#common-commands-cheat-sheet)
4. [Real-World Scenarios](#real-world-scenarios)
5. [When to Use Branches vs Direct Commits](#when-to-use-branches-vs-direct-commits)
6. [Troubleshooting](#troubleshooting)

---

## Basic Concepts

### What is Git?
- **Version control system** that tracks changes to your code
- Lets you save "snapshots" (commits) of your project
- Allows multiple versions (branches) to exist simultaneously

### Key Terms
- **Repository (repo)**: Your project folder tracked by Git
- **Commit**: A saved snapshot of your code with a message
- **Branch**: A separate line of development
- **main**: The primary/production branch (always working code)
- **Merge**: Combining changes from one branch into another
- **Remote**: The online version (e.g., GitHub)
- **Origin**: Default name for your remote repository

---

## Feature Branch Workflow

### The Golden Rule
**`main` = always working code. Features = separate branches.**

### Complete Workflow (5 Steps)

```bash
# Step 1: Start from clean main
git checkout main
git pull origin main

# Step 2: Create feature branch
git checkout -b feature/feature-name

# Step 3: Work + commit (repeat as needed)
git add .
git commit -m "feat: descriptive message"

# Step 4: Merge when feature complete
git checkout main
git pull origin main  # Get latest changes
git merge feature/feature-name

# Step 5: Push + cleanup
git push origin main
git branch -d feature/feature-name  # Delete local branch
```

---

## Common Commands Cheat Sheet

### Starting a Project
```bash
git init                    # Initialize Git in current folder
git add .                   # Stage all files
git commit -m "message"     # Create first commit
git remote add origin URL   # Connect to GitHub
git push -u origin main     # Push to GitHub
```

### Daily Workflow
```bash
# Check status
git status                  # See what's changed
git branch                  # See all branches (* = current)
git log --oneline           # See commit history

# Making changes
git add filename.py         # Stage specific file
git add .                   # Stage all changes
git commit -m "message"     # Commit staged changes

# Switching branches
git checkout main           # Switch to main
git checkout -b new-branch  # Create + switch to new branch

# Syncing with remote
git pull origin main        # Get latest from GitHub
git push origin main        # Send commits to GitHub
```

### Branch Management
```bash
# Create branch (2 ways)
git checkout -b feature/name    # Classic (create + switch)
git branch feature/name         # Modern (create only)
git switch feature/name         # Modern (switch only)

# View branches
git branch                  # Local branches
git branch -v               # Local branches + last commit
git branch -a               # All branches (local + remote)

# Delete branches
git branch -d feature/name  # Delete local branch
git push origin --delete feature/name  # Delete remote branch
```

### Merging
```bash
# Standard merge
git checkout main           # Go to target branch
git merge feature/name      # Merge feature into main

# Check merge status
git log --oneline --graph   # Visual branch history
```

---

## Real-World Scenarios

### Scenario 1: Adding Master Password Feature
```bash
# On main with working password manager
git checkout main
git checkout -b feature/master-password

# Make changes, test
# ... code ...

git add .
git commit -m "feat: add master password protection with sha256"

# Ready to merge
git checkout main
git pull origin main
git merge feature/master-password
git push origin main
git branch -d feature/master-password
```

### Scenario 2: Multiple Features in Parallel
```bash
# Working on feature A
git checkout -b feature/password-generator
# ... work on generator ...
git commit -m "feat: add password generator"

# Need to start feature B before A is done
git checkout main
git checkout -b feature/file-encryption
# ... work on encryption ...
git commit -m "feat: add file encryption"

# Finish A first
git checkout main
git merge feature/password-generator
git push origin main

# Later finish B
git checkout main
git merge feature/file-encryption
git push origin main
```

### Scenario 3: Accidentally Broke Something
```bash
# Working on feature/new-feature
# ... made changes that broke code ...

# Option 1: Undo uncommitted changes
git checkout .              # Discard all changes

# Option 2: Go back to main (working version)
git checkout main           # Main still works!
git branch -D feature/new-feature  # Force delete broken branch
git checkout -b feature/new-feature  # Start fresh
```

---

## When to Use Branches vs Direct Commits

### Use Feature Branches When:
✅ Adding a new feature (master password, encryption)  
✅ Experimenting with changes  
✅ Working on something that takes multiple commits  
✅ Want to keep main always working  
✅ Collaborating with others (always!)  

### Direct Commits to Main Okay When:
✅ Solo project < 300 lines  
✅ Quick typo fixes  
✅ README updates  
✅ Very small bug fixes  

### Professional Projects (Job Context)
**Always use feature branches** + pull requests for code review.

---

## Branch Naming Conventions

Use prefixes to organize branches:

```bash
feature/master-password     # New functionality
feature/password-generator
feature/file-encryption

fix/search-crash           # Bug fixes
fix/typo-in-menu

hotfix/security-patch      # Urgent production fixes

refactor/split-files       # Code restructuring
refactor/improve-ui

docs/update-readme         # Documentation only
```

---

## Troubleshooting

### "Please commit your changes or stash them before you merge"
**Problem**: Uncommitted changes on current branch  
**Solution**:
```bash
git add .
git commit -m "message"
# OR
git stash  # Temporarily save changes
```

### "Your branch is behind 'origin/main'"
**Problem**: Remote has newer commits  
**Solution**:
```bash
git pull origin main
```

### "Merge conflict in file.py"
**Problem**: Same lines changed in both branches  
**Solution**:
```bash
# Open file.py, look for:
<<<<<<< HEAD
your code
=======
their code
>>>>>>> feature/branch

# Manually choose which to keep, remove markers
git add file.py
git commit -m "fix: resolve merge conflict"
```

### "fatal: not a git repository"
**Problem**: Not in a Git-tracked folder  
**Solution**:
```bash
git init  # Initialize Git
```

### Committed to wrong branch
**Problem**: Made commit on main instead of feature branch  
**Solution**:
```bash
git log --oneline  # Note commit hash (e.g., abc1234)
git reset --hard HEAD~1  # Undo commit on main
git checkout -b feature/correct-branch
git cherry-pick abc1234  # Apply commit to new branch
```

---

## Quick Reference: The 3-Step Cycle

For every improvement to your password manager:

```
1. Branch  → git checkout -b feature/name
2. Work    → code + git commit
3. Merge   → git checkout main + git merge
```

**Repeat 11 times for 11 features = professional portfolio project!**

---

## Commit Message Best Practices

### Format
```
type: brief description (50 chars max)

Optional longer explanation if needed.
```

### Types
- `feat:` New feature (feat: add master password)
- `fix:` Bug fix (fix: handle empty password file)
- `refactor:` Code restructuring (refactor: split into modules)
- `docs:` Documentation (docs: update README)
- `style:` Formatting (style: fix indentation)
- `test:` Adding tests (test: add password validation tests)

### Examples
```bash
git commit -m "feat: add password generator with configurable length"
git commit -m "fix: prevent crash when password.txt missing"
git commit -m "refactor: extract encryption logic to separate module"
```

---

## Your Password Manager: 11-Feature Plan

Using feature branches for each:

```
main ──┬─ feature/master-password ──────── merged ✅
       ├─ feature/password-generator ────── merged
       ├─ feature/file-encryption ───────── merged
       ├─ feature/delete-credential ────── merged
       ├─ feature/password-strength ────── merged
       ├─ feature/case-insensitive-search ─ merged
       ├─ feature/auto-sort ────────────── merged
       ├─ feature/backup-export ─────────── merged
       ├─ feature/getpass-everywhere ───── merged
       ├─ feature/clear-screen ─────────── merged
       └─ feature/auto-lock ────────────── merged
```

Each branch = safe, isolated, professional.

---

## Interview Talking Points

When discussing your password manager in interviews:

> "I used a feature branch workflow with 11 separate branches for each enhancement. This kept the main branch deployable at all times and gave me atomic commits that were easy to review and rollback if needed."

> "For example, when adding master password protection, I created `feature/master-password`, implemented the hashing with SHA-256, tested it thoroughly, then merged to main only when it was production-ready."

> "Each feature branch was merged via pull request after self-review, demonstrating the same workflow used in professional development teams."

---

## Advanced: When You're Ready

### Rebasing (alternative to merging)
```bash
git checkout feature/name
git rebase main  # Replay your commits on top of main
```

### Interactive Rebase (clean up history)
```bash
git rebase -i HEAD~3  # Edit last 3 commits
```

### Stashing (save work temporarily)
```bash
git stash           # Save changes
git stash pop       # Restore changes
git stash list      # See all stashes
```

---

## Summary: Your Git Superpowers

✅ **Feature branches** = safe experimentation  
✅ **main** = always working code  
✅ **Commits** = save points you can return to  
✅ **Merge** = integrate features safely  
✅ **Pull** = sync with remote/team  
✅ **Push** = share your work  

**You now have professional version control skills!**

---

*Created: February 2026*  
*For: First-year CS student Python projects*  
*Context: Shopping List Manager → Password Manager (11 features)*
