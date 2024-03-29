

from enum import Enum

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from uvicorn import run as uvi_run

app = FastAPI()

class TaskStatus(str, Enum):
    pending = "pending"
    completed = "completed"

class Task(BaseModel):
    title: str
    description: str
    status: TaskStatus

tasks = []

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Welcome to the Task Manager</h1>"

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    try:
        return tasks[task_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    try:
        tasks[task_id] = task
        return task
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        deleted_task = tasks.pop(task_id)
        return deleted_task
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    uvi_run(app, host="127.0.0.1", port=8000)

