# 🚀 Task Manager API (FastAPI)

A backend REST API built using **FastAPI** for managing users and their tasks with full CRUD functionality, filtering, and relationship handling.

This project focuses on real-world backend concepts such as validation, business logic, data relationships, and proper HTTP error handling.

---

## ✨ Features

### 👤 User Management

* Create users
* View all users

### 📋 Task Management

* Create tasks for users
* View all tasks
* Update tasks
* Delete tasks

### 🔍 Filtering & Queries

* Filter tasks by status (pending / completed)
* Filter tasks by user
* Filter tasks by user + status

### ⚠ Error Handling

* Prevent duplicate users & tasks
* Validate user existence before task creation
* Proper HTTP status codes

---

## 🛠 Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## 📁 Project Structure

```
task-manager-api/
│
├── app/
│   └── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶ Run Locally

### Install dependencies:

```bash
pip install fastapi uvicorn pydantic
```

### Start server:

```bash
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Users

| Method | Endpoint | Description   |
| ------ | -------- | ------------- |
| POST   | /users   | Create user   |
| GET    | /users   | Get all users |

### Tasks

| Method | Endpoint                         | Description             |
| ------ | -------------------------------- | ----------------------- |
| POST   | /tasks                           | Create task             |
| GET    | /tasks                           | Get all tasks           |
| GET    | /tasks/user/{user_id}            | Get tasks of user       |
| GET    | /tasks/status/{status}           | Filter by status        |
| GET    | /tasks/user/{id}/status/{status} | Filter by user + status |
| PUT    | /tasks/{id}                      | Update task             |
| DELETE | /tasks/{id}                      | Delete task             |

---

## 🎯 Learning Goals

This project was built to master:

* REST API design
* CRUD operations
* Data validation
* Relationship handling
* Filtering & querying logic
* Proper backend error handling

---

## 🚀 Future Improvements

* Database integration (PostgreSQL)
* Authentication & authorization
* Pagination & search
* Deployment

---

## 👨‍💻 Author

Dhruv Kashyap

---
