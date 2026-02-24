from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users_db = []
tasks_db = []

class User(BaseModel):
    id : int
    name : str
    email: str

class Task(BaseModel):
    id : int
    title : str
    description : str
    status : str          # pending or completed
    user_id : int

# create user
@app.post("/users", status_code=status.HTTP_201_CREATED )
def create_user(user : User):
    for items in users_db:
        if items.id == user.id:
            raise HTTPException(400, "User already exists")

    users_db.append(user)
    return user

# get user
@app.get("/users", response_model=List[User])
def get_all_users():
    return users_db

# create task for user
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task : Task):
    # check user exists
    user_found = False
    for item in users_db:
        if item.id == task.user_id:
            user_found = True
            break
    if not user_found:
        raise HTTPException(404, "user not found")

    # check duplicate task id
    for items in tasks_db:
        if items.id == task.id:
            raise HTTPException(400, "Task already exists")

    tasks_db.append(task)
    return task

# get all tasks
@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    return tasks_db

# filter tasks by user + status
@app.get("/tasks/user/{id}/status/{status}")
def task_user_status_tasks(id: int, status: str):

    filtered = []

    for task in tasks_db:
        if task.user_id == id and task.status.lower() == status.lower():
            filtered.append(task)

    if not filtered:
        raise HTTPException(404, "No tasks found")

    return filtered

# filter task by status
@app.get("/tasks/status/{status}")
def task_status(status: str):

    filtered = []

    for task in tasks_db:
        if task.status.lower() == status.lower():
            filtered.append(task)

    if not filtered:
        raise HTTPException(404, "No tasks found")

    return filtered

# get task of a user
@app.get("/tasks/user/{user_id}")
def get_task(user_id : int):
    user_tasks = []

    for tasks in tasks_db:
        if tasks.user_id == user_id:
            user_tasks.append(tasks)
    if not user_tasks:
        raise HTTPException(404, "No tasks for this user")

    return user_tasks

# update task
@app.put("/tasks/{id}")
def update_task(id : int, updated : Task):
    for index, task in enumerate(tasks_db):
        if task.id == id:
            tasks_db[index] = updated
            return updated

    raise HTTPException(404, "Task not found")

# delete task
@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id : int):
    for tasks in tasks_db:
        if tasks.id == id:
            tasks_db.remove(tasks)
            return

    raise HTTPException(404, "Task not found")




