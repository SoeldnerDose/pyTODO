import uuid
from abc import ABC, abstractmethod
from fastapi import HTTPException
from models import TodoCreateUpdate, Todo, User

# Abstract class for TodoStorage
class TodoStorage(ABC):
    @abstractmethod
    async def create_todo(self, todo: TodoCreateUpdate, user: User) -> Todo:
        pass

    @abstractmethod
    async def read_todos(self, user: User, skip: int = 0, limit: int = 10) -> list[Todo]:
        pass

    @abstractmethod
    async def read_todo_by_uid(self, uid: str) -> Todo:
        pass

    @abstractmethod
    async def update_todo(self, user: User, uid: str, updated_todo: TodoCreateUpdate) -> Todo:
        pass

    @abstractmethod
    async def delete_todo(self, user: User, uid: str) -> Todo:
        pass

# In-memory implementation of TodoStorage
class InMemoryTodoStorage(TodoStorage):
    todos_db = []

    async def create_todo(self, todo: TodoCreateUpdate, user: User) -> Todo:
        new_todo = Todo(
            uid=str(uuid.uuid4()),
            title=todo.title,
            description=todo.description,
            state=todo.state,
            user=user
        )
        self.todos_db.append(new_todo)
        return new_todo

    async def read_todos(self, user: User, skip: int = 0, limit: int = 10) -> list[Todo]:
        return [t for t in self.todos_db if t.user == user][skip:skip + limit]

    async def read_todo_by_uid(self, uid: str) -> Todo:
        todo = next((t for t in self.todos_db if t.uid == uid), None)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    async def update_todo(self, user: User, uid: str, updated_todo: TodoCreateUpdate) -> Todo:
        todo = next((t for t in self.todos_db if t.uid == uid and t.user == user), None)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        todo.title = updated_todo.title
        todo.description = updated_todo.description
        todo.state = updated_todo.state
        return todo

    async def delete_todo(self, user: User, uid: str) -> Todo:
        todo = next((t for t in self.todos_db if t.uid == uid and t.user == user), None)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        self.todos_db.remove(todo)
        return todo
