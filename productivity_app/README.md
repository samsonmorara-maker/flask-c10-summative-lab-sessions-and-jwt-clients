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

```bash
git clone <your-repository-url>
cd productivity_app