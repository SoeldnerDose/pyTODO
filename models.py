from pydantic import BaseModel
from enum import Enum

# Enum for todo states
class TodoState(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

# Model for User
class User(BaseModel):
    username: str

# Model for creating/updating Todo
class TodoCreateUpdate(BaseModel):
    title: str
    description: str
    state: TodoState

# Model for Todo
class Todo(BaseModel):
    uid: str
    title: str
    description: str
    state: TodoState
    user: User
