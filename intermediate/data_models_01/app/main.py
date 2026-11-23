# Blog API - Lesson 1: Main Application
# Create FastAPI endpoints to demonstrate data models

from fastapi import FastAPI, HTTPException
from datetime import datetime

# TODO: Import your models fro-m the models module
# from .models import UserRole, User, BlogPost, UserCreate, BlogPostResponse
from .models import UserRole, User, BlogPost, UserCreate, BlogPostResponse

# TODO: Create FastAPI application
# Replace with FastAPI(title="Blog API - Data Models", ...)
app = FastAPI(title='Blog API - Data Models')

# TODO: Add root endpoint GET /
# Return: {"message": "Welcome to Blog API - Data Models Demo",
#          "version": "1.0.0",
#          "lesson": "Data Models Deep Dive"}
@app.get("/")
async def root():
    return {
        "message": "Welcome to Blog API - Data Models Demo",
        "version": "1.0.0",
        "lesson": "Data Models Deep Dive"
    }

# TODO: Add GET /models/demo endpoint
# Create sample User, BlogPost, and BlogPostResponse instances
# Return: {"message": "Data model examples",
#          "models": {"user": ..., "blog_post": ..., "blog_post_with_author": ...},
#          "available_roles": [role.value for role in UserRole]}
@app.get("/models/demo")
async def get_demo():
    return {
        "message": "Data model examples",
        "models": {},
        "available_roles": [role.value for role in UserRole]
    }

# TODO: Add POST /models/validate-user endpoint
# Accept a UserCreate body and report on what came through:
# Return: {"message": "User data is valid!",
#          "validated_data": {"username": ..., "email": ..., "full_name": ...,
#                             "password_length": len(password),
#                             "password_has_number": True/False},
#          "validation_passed": True}
@app.post("/models/validate-user")
async def create_user(user_create: UserCreate):
    return {
        "message": "User data is valid!",
        "validated_data": {
            "username": user_create.username,
            "email": user_create.email,
            "full_name": user_create.full_name,
            "password_length": len(user_create.password),
            "password_has_number": True,
        },
        "validation_passed": True
    }

# TODO: Add POST /models/validate-post endpoint
# Accept a BlogPost body and report on what came through:
# Return: {"message": "Blog post data is valid!",
#          "validated_data": {"title": ..., "content_length": len(content),
#                             "author_id": ..., "tags": ...,
#                             "tag_count": len(tags), "published": ...},
#          "validation_passed": True}
@app.post("/models/validate-post")
async def validate_post(blog_post: BlogPost):
    return {
        "message": "Blog post data is valid!",
        "validated_data": {
            "title": blog_post.title,
            "content_length": len(blog_post.content),
            "author_id": blog_post.author_id,
            "tags": blog_post.tags,
            "tag_count": len(blog_post.tags),
            "published": blog_post.published
        },
        "validation_passed": True
    }

# TODO: Add GET /models/schema/{model_name} endpoint
# Return JSON schema for user, blog_post, user_create, or blog_post_response:
# {"model_name": model_name, "schema": User.model_json_schema()} (etc.),
# and a 404 for any other name
@app.get("/models/schema/{model_name}")
async def get_model(model_name: str):
    if model_name == 'user':
        model = User
    elif model_name == 'blog_post':
        model = BlogPost
    elif model_name == 'user_create':
        model = UserCreate
    elif model_name == 'blog_post_response':
        model = BlogPostResponse
    else:
        raise HTTPException(detail="Invalid model name", status_code=404)
    return {
        "model_name": model_name,
        "schema": model.model_json_schema()
    }


# TODO: Add GET /models/roles endpoint
# Return: {"roles": [{"value": role.value, "name": role.name} for each role],
#          "default_role": UserRole.READER.value}
@app.get("/models/roles")
async def get_roles():
    return {
        "roles": [
            {"value": role.value, "name": role.name} for role in UserRole
        ],
        "default_role": UserRole.READER.value
    }
