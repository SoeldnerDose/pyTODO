from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo():
    def __init__(self, id: int, description: str, status: bool):
        self.id = id
        self.description = description
        self.status = status

class TodoBaseModel(BaseModel):
    id: int
    description: str
    status: bool

todos = [Todo(1, "Müll rausbringen", False), Todo(2, "Wäsche waschen", False), Todo(3, "Hühner füttern", False)]

@app.get("/")
async def root():
    return {"message": "Welcome to your Todo Buddy"}

@app.get("/getTodos", response_model=list[TodoBaseModel])
async def getTodos() -> list[TodoBaseModel]:
    return todos

@app.get("/getTodo/{todo_id}", response_model=TodoBaseModel)
async def getTodo(todo_id) -> TodoBaseModel:
    return todos[int(todo_id)]