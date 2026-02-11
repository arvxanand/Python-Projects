# Password Manager (Python CLI)

A simple command-line password manager written in Python.  
It lets you create a master password, then add, view, search, and delete saved login credentials. Credentials are stored locally in a text file.

## Features
- Master password protection (SHA-256 hash stored locally)
- Add credentials (site + username + password)
- Generate a random password using Python’s `secrets` module
- View saved credentials (site + username)
- Search credentials by site name
- Delete credentials by site name
- Loading animation for a nicer CLI feel

## How it works
- On first run, the program creates a **master password hash** and stores it in `master_hash.txt`.
- After you enter the correct master password, you can manage credentials.
- Credentials are stored in `password.txt` using this format:
  ```
  site:username:password
  ```

## Requirements
- Python 3.8+ recommended (should work on most Python 3 versions)

Uses only built-in libraries:
- `hashlib`, `getpass`, `sys`, `time`, `secrets`, `string`

## Setup
1. Clone the repo:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Run the program:
   ```bash
   python main.py
   ```
   (If your file is named something else, run that filename instead.)

## Usage
When you start the program:
1. If there is no master password yet, you’ll be asked to create one.
2. You’ll then be asked to enter the master password to unlock access.
3. After that, use the menu options:

- **1** Add credentials  
- **2** View all saved credentials  
- **3** Search by site  
- **4** Delete credentials  
- **5** Quit  

### Password Generation
If you choose **Generated**, the program asks for a password length and generates one using letters + numbers.

## Files Created
This project stores data locally in two files:
- `master_hash.txt` — stores the SHA-256 hash of your master password
- `password.txt` — stores credentials as `site:username:password`

> Tip: Add these files to `.gitignore` so you don’t upload private data to GitHub.

Example `.gitignore`:
```gitignore
password.txt
master_hash.txt
```

## Security Notes (important)
This is a learning project and not meant to be a secure production password manager.
- Passwords are stored in **plain text** in `password.txt`.
- The master password is hashed, but there is no encryption protecting the saved passwords.

If you want to improve security later, good upgrades are:
- Encrypt `password.txt` (e.g., using `cryptography` / Fernet)
- Add special characters to generated passwords
- Add locking after multiple failed attempts
- Improve searching (case-insensitive + partial matches)

## Known Issues / Things to Improve
A few things you may want to fix/upgrade:
- If the user types something invalid for password length, it can crash (needs input checking)
- Search currently only matches exact site names
- Delete removes from the file, but the in-memory list can still contain old data until reload
- Generated password function can be cleaned up to handle empty input better


