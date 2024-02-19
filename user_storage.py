from abc import ABC, abstractmethod
from fastapi import HTTPException
from models import User

# Abstract class for UserStorage
class UserStorage(ABC):
    @abstractmethod
    async def verify_user_exists(self, user: User) -> bool:
        pass

    @abstractmethod
    async def validate_user(self, user: User) -> None:
        pass

# Simple in-memory implementation of UserStorage
class InMemoryUserStorage(UserStorage):
    users_db = ["john_doe", "jane_doe"]

    async def verify_user_exists(self, user: User) -> bool:
        return user.username in self.users_db

    async def validate_user(self, user: User) -> None:
        if not await self.verify_user_exists(user):
            raise HTTPException(status_code=401, detail="User not authorized")
