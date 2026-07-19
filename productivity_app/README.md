# Productivity Notes

## Description

A secure Flask REST API that allows users to create and manage personal notes. 
The application uses JWT authentication and ensures users can only access and modify their own notes.

## Features

- User registration
- User login with JWT authentication
- Secure password hashing with Flask-Bcrypt
- Protected API routes
- User-owned notes
- Create, read, update, and delete notes
- Pagination on notes endpoint
- Database migrations using Flask-Migrate

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-JWT-Extended
- SQLite
- Pipenv

---

# Installation

## 1. Clone the repository


git clone https://github.com/samsonmorara-maker/flask-c10-summative-lab-sessions-and-jwt-clients.git
cd productivity_app

## 2.Install dependencies
pipenv shell
## 3.Running the Application
flask --app app run
## author 
developed by Manoti Samson