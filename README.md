# OS Library Project

A Python-based file management and library project developed using the `os` module.

The project includes a simple login system with three access levels: Free, Premium, and Admin.

## Features

* User login with username and password
* Three access levels:

  * Free
  * Premium
  * Admin
* Create a new folder
* Check whether a file exists
* List files inside a folder in sorted order
* Display the full folder tree for Premium and Admin users
* Register new users as an Admin
* Colored terminal output using Colorama
* File and folder management using Python's `os` module

## Technologies

* Python
* `os`
* `colorama`

## Access Levels

### Free

Free users can:

* Create a new folder
* Check if a file exists
* List files in a folder

### Premium

Premium users have all Free features plus:

* Access to the full folder tree

### Admin

Admin users have all Premium features plus:

* Register new users

## Requirements

Install the required package with:

```bash
pip install -r requirements.txt
```

## How to Run

Run the project with:

```bash
python os_project.py
```

Then enter a valid username and password.

## Project Structure

```text
OS-Library-Project/
│
├── os_project.py
├── README.md
├── requirements.txt
└── Demo/
    ├── Action/
    ├── Comedy/
    ├── Crime/
    └── Documentary/
```

## Demo Folder

The `Demo` folder contains the sample folders and files used by the program.

The project uses a relative path to the `Demo` folder, so the project can be moved to another computer without changing an absolute Windows path.

## Notes

This project is created for educational purposes to practice Python file and folder management, access control, functions, and the `os` module.
