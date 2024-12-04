from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()

# Task Model
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime = datetime.now()

tasks = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.post("/tasks/add")
async def post_tasks(task: Task):
    task.id = str(uuid())
    tasks.append(task.dict())
    return tasks

@app.get("/tasks/{id}")
def get_task(id: str):
    print(id)
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")