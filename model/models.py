from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=120)
    email: Optional[str] = None


class UserResponse(User):
    id: str


