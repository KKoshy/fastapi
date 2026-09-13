# Body - Multiple Parameters - Complete Tutorial
# Following the official FastAPI tutorial - all 5 concepts

from typing import Union
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

# Pydantic models for request bodies
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

# TODO 1: Mix Path, Query and body parameters
# Create endpoint PUT /items/{item_id}/basic
# Parameters: item_id (Path with validation), q (optional query), item (optional body)
# Use Path(title="The ID of the item to get", ge=0, le=1000) for item_id
# Return results dict with item_id, and conditionally add q and item if provided
@app.put("/items/{item_id}/basic")
# * separates the positional arguments from keyword arguments
async def update_item_basic(item_id: int = Path(title='The ID of the item to get', ge=0, le=1000), *, item: Item|None=None, q: str|None=None):
                results = {"item_id": item_id}
                if q:
                    results["q"] = q
                if item:
                    results["item"] = item
                return results

# TODO 2: Multiple body parameters (main concept)
# Create endpoint PUT /items/{item_id}
# Parameters: item_id (int), item (Item), user (User)
# Return: {"item_id": item_id, "item": item, "user": user}
@app.put("/items/{item_id}")
async def update_item(item_id: int, *, item: Item, user: User):
                return {"item_id": item_id, "item": item, "user": user}

# TODO 3: Singular values in body
# Create endpoint PUT /items/{item_id}/importance
# Parameters: item_id, item (Item), user (User), importance (int = Body())
# Return: dict with all parameters
@app.put("/items/{item_id}/importance")
async def update_item_importance(item_id: int, *, item: Item, user: User, importance: int=Body()):
                return {"item_id": item_id, "item": item, "user": user, "importance": importance}

# TODO 4: Multiple body params and query
# Create endpoint PUT /items/{item_id}/full
# Parameters: item_id, item, user, importance (Body(gt=0)), q (optional query)
# Use * to force keyword-only arguments
# Return: dict with all params, conditionally add q
@app.put("/items/{item_id}/full")
async def upate_item_full(item_id: int, *, item: Item, user: User, importance: int|None=Body(gt=0), q: str|None=None):
                results = {"item_id": item_id, "item": item, "user": user}
                if q:
                    results["q"] = q
                if importance:
                    results["importance"] = importance
                return results

# TODO 5: Embed single body parameter
# Create endpoint PUT /items/{item_id}/embed
# Parameters: item_id, item (Item = Body(embed=True))
# Return: {"item_id": item_id, "item": item}
@app.put("/items/{item_id}/embed")
async def update_item_embed(item_id: int, *, item: Item=Body(embed=True)):
        return {"item_id": item_id, "item": item}
