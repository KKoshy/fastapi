# Blog API - Lesson 1: Data Models
# Define Pydantic models for the blog API

from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from typing import Optional, List
from datetime import datetime
from enum import Enum
import re

# TODO: Define UserRole enum with values: ADMIN, AUTHOR, READER
class UserRole(str, Enum):
    # Replace with enum values
    ADMIN = "admin"
    AUTHOR = "author"
    READER = "reader"

# TODO: Create User model with validation
# Fields: id (Optional[int], default None),
#         username (str, 3-20 chars, alphanumeric+underscore),
#         email (EmailStr), full_name (Optional[str], default None),
#         role (UserRole, default UserRole.READER), is_active (bool, default True),
#         created_at (Optional[datetime], default None)
class User(BaseModel):
    # Implement the User model
    id: Optional[int] = Field(default=None)
    username: str = Field(min_length=3, max_length=20,
                                          pattern=r'[a-zA-Z0-9_]+')
    email: str
    full_name: Optional[str] = Field(default=None)
    role: UserRole = Field(default=UserRole.READER)
    is_active: bool = Field(default=True)
    created_at : Optional[datetime] = Field(default=None)

# TODO: Create BlogPost model with validation
# Fields: id (Optional[int], default None), title (str, 1-200 chars),
#         content (str, min 10 chars), author_id (int),
#         tags (List[str], default []), published (bool, default False),
#         created_at (Optional[datetime], default None),
#         updated_at (Optional[datetime], default None)
# Fields with a default may be left out of a request body; the rest are required.
# Add a field_validator for tags: each tag 1-20 chars, alphanumeric + hyphens + underscores
class BlogPost(BaseModel):
    id : Optional[int] = Field(default=None)
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=10)
    author_id : int
    tags : List[str] = Field(default_factory=[])
    published: bool = Field(default=False)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, tags: List[str]) -> List[str]:
        pattern = r"^[a-zA-Z0-9_-]{1,20}$"

        for tag in tags:
            if not re.fullmatch(pattern, tag):
                raise ValueError("Tag does not match pattern")
        return tags

# TODO: Create UserCreate schema for registration
# Fields: username and email (validated as in User), full_name (Optional[str], default None),
#         password (min 8 chars, must contain a number)
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20,
                                          pattern=r'[a-zA-Z0-9_]+')
    email: str
    full_name: Optional[str] = Field(default=None)
    password: str = Field(min_length=8)

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str :
        if len(password) <8:
            raise ValueError("Incorrect password length")
        elif not re.search(r'\d', password):
            raise ValueError("Password does not have a number")
        return password

# TODO: Create BlogPostResponse with nested author
# Inherit from BlogPost, add author: User field
class BlogPostResponse(BlogPost):
    author: User 
