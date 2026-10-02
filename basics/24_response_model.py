from enum import Enum
from typing import Set, Union

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


class Tags(Enum):
    items = "items"
    users = "users"


# TODO: Create a POST endpoint for items with status.HTTP_201_CREATED status code
# Use @app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
# Return the item it was given - response_model=Item shapes the response
@app.post("/items/", status_code=status.HTTP_201_CREATED, response_model=Item)
async def create_items(item: Item):
    return item


# TODO: Create a GET endpoint for items with "items" tag
# Use @app.get("/items/", tags=["items"])
# Return: [{"name": "Foo", "price": 42}]
@app.get("/items/", tags=["items"])
async def get_item():
    return [{"name": "Foo", "price": 42}]


# TODO: Create a GET endpoint for users with "users" tag
# Use @app.get("/users/", tags=["users"])
# Return: [{"username": "johndoe"}]
@app.get("/users/", tags=["users"])
async def get_users():
    return  [{"username": "johndoe"}]


# TODO: Create a GET endpoint for elements with Tags.items enum tag
# Use @app.get("/elements/", tags=[Tags.items])
@app.get("/elements/", tags=[Tags.items])
async def get_elements():
    return [{"item_id": "Foo"}]


# TODO: Create a POST endpoint with summary and description
# Use @app.post("/items-summary/", response_model=Item, summary="Create an item", description="...")
@app.post("/items-summary/", response_model=Item, summary="Create an item", description="....")
async def create_item_summary(item: Item):
    return item


# TODO: Create a POST endpoint with docstring description
# Use @app.post("/items-docstring/", response_model=Item, summary="Create an item")
# Add a detailed docstring with markdown
@app.post("/items-docstring/", response_model=Item, summary="Create an item")
async def create_docstring(item: Item):
    return item


# TODO: Create a deprecated GET endpoint for elements
# Use @app.get("/elements/", tags=["items"], deprecated=True)
# Return: [{"item_id": "Foo"}]
@app.get("/elements/", tags=["items"], deprecated=True)
async def get_elements():
    return [{"item_id": "Foo"}]
