from fastapi import FastAPI, Depends, Header
from user_storage import InMemoryUserStorage
from todo_storage import InMemoryTodoStorage
from models import User, TodoCreateUpdate, Todo

app = FastAPI()

# Create instances of InMemoryUserStorage and InMemoryTodoStorage
user_storage = InMemoryUserStorage()
todo_storage = InMemoryTodoStorage()

# Helper function to get current user from request and validate against user storage
async def get_current_user(username: str = Header(..., convert_underscores=False)):
    user = User(username=username)
    await user_storage.validate_user(user)
    return user

# CRUD operations using the abstracted storage and current user dependency
@app.post("/todos/", response_model=Todo)
async def create_todo(todo: TodoCreateUpdate, user: User = Depends(get_current_user)):
    return await todo_storage.create_todo(todo, user)

@app.get("/todos/", response_model=list[Todo])
async def read_todos(user: User = Depends(get_current_user), skip: int = 0, limit: int = 10):
    return await todo_storage.read_todos(user, skip, limit)

@app.get("/todos/{uid}", response_model=Todo)
async def read_todo_by_uid(uid: str):
    return await todo_storage.read_todo_by_uid(uid)

@app.put("/todos/{uid}", response_model=Todo)
async def update_todo(uid: str, updated_todo: TodoCreateUpdate, user: User = Depends(get_current_user)):
    return await todo_storage.update_todo(user, uid, updated_todo)

@app.delete("/todos/{uid}", response_model=Todo)
async def delete_todo(uid: str, user: User = Depends(get_current_user)):
    return await todo_storage.delete_todo(user, uid)
