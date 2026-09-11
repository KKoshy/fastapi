# Path Parameters
# Learn to create dynamic URLs that capture values from the URL path

from fastapi import FastAPI

app = FastAPI()

# TODO: Create a GET endpoint at "/items/{item_id}" 
# The function should:
# - Accept item_id as a parameter (no type hint initially)
# - Return {"item_id": item_id}
# Hint: @app.get("/items/{item_id}")
@app.get("/items/{item_id}")
async def get_item(item_id):
    return {"item_id": item_id}

# TODO: Create a GET endpoint at "/items/{item_id}/typed"
# The function should:
# - Accept item_id as an integer (use type hint: item_id: int)
# - Return {"item_id": item_id}
# This demonstrates automatic type conversion!
@app.get("/items/{item_id}/typed")
async def get_item_types(item_id: int):
    return {"item_id": item_id}

# TODO: Create a GET endpoint at "/users/me"
# The function should:
# - Take no parameters
# - Return {"user_id": "the current user"}
# This must come BEFORE the variable path!
@app.get("/users/me")
async def get_current_user():
    return {"user_id": "the current user"}

# TODO: Create a GET endpoint at "/users/{user_id}"
# The function should:
# - Accept user_id as a string parameter
# - Return {"user_id": user_id}
@app.get("/users/{user_id}")
async def get_user_id(user_id: str):
    return {"user_id": user_id}
