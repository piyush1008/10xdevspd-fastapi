from pydantic import BaseModel, Field, field_validator, Annotated
from typing import Optional


class User(BaseModel):
    username: Annotated[str, Field(..., description="Username", examples='pd01')]
    password: str
    name: Optional[str] = Field(..., min_length=3, max_length=50)
    age: Optional[int] = Field(..., ge=18, le=120)
    email: Optional[str] = None

    @field_validator(age)
    @classmethod
    def validate_age(cls, value):
        if age<0 and age >100:
            return ValueError("age must be greater than 0 and less than 100")
        return value

class UserResponse(User):
    id: str

class Post(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    content: str = Field(..., min_length=3, max_length=500)
    author_id: str

class PostResponse(Post):
    id: str
