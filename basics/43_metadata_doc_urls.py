from fastapi import FastAPI

# TODO: Create a description for your API using Markdown
# Include sections for Items and Users
# Example format:
# """
# Task Management API description here. 🚀
#
# ## Items
# Description of items functionality
#
# ## Users
# Description of users functionality
# """
description = """
Task Management API description here. 🚀

## Items
Description of items functionality

## Users
Description of users functionality
 """

# TODO: Define metadata for tags
# Create a list with two dictionaries for 'users' and 'items' tags, in that order
# Each should have: name, description, and optionally externalDocs
tags_metadata = [
    {"name": "users", "description": "supports users functionality"},
    {"name": "items", "description": "supports items functionality"}
]

# TODO: Create FastAPI application with metadata
# Include: title, description, summary, version, terms_of_service,
# contact (name, url, email), license_info (name, url),
# and openapi_tags
# The checks read /openapi.json for: title="Task Management API",
# version="1.0.0", a license named "MIT", and the 'users' and 'items' tags
app = FastAPI(
    title="Task Management API",
    description=description,
    summary="A simple and efficient task manager",
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "API support team",
        "url": "http://example.com/contact/",
        "email": "support@example.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    openapi_tags=tags_metadata
)


@app.get("/")
async def root():
    """Root endpoint to verify the API is running."""
    # TODO: Return a welcome message
    # Return: {"message": "Welcome to Task Management API"}
    return  {"message": "Welcome to Task Management API"}


# TODO: Add tags=["items"] to this endpoint
@app.get("/items/", tags=["items"])
async def read_items():
    """Get all available items."""
    # TODO: Return a list of items
    # Return: [{"id": 1, "name": "Task Manager"}, {"id": 2, "name": "Code Editor"}]
    return  [{"id": 1, "name": "Task Manager"}, {"id": 2, "name": "Code Editor"}]


# TODO: Add tags=["users"] to this endpoint
@app.get("/users/", tags=["users"])
async def read_users():
    """Get all users."""
    # TODO: Return a list of users
    # Return: [{"username": "johndoe"}, {"username": "janedoe"}]
    return [{"username": "johndoe"}, {"username": "janedoe"}]
