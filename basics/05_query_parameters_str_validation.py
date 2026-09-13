# Query Parameters and String Validations - Following Official FastAPI Tutorial
# Learn how to add validation and constraints to query parameters
from typing import Annotated
from fastapi import FastAPI, Query
# TODO: Import Query from fastapi

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Step 1: Add validation to query parameters
# TODO: Create a GET endpoint at "/items/"
# TODO: Add parameter: q: str | None = Query(default=None, max_length=50)
# TODO: Return items filtered by q if provided, or all items if q is None
# Hint: Use Query() instead of just setting default values
@app.get("/items/")
async def get_items(q: str|None = Query(default=None, max_length=50)):
                items = fake_items_db
                if q:
                    items = [x for x in fake_items_db if q in x["item_name"]]
                return items

# Step 2: Add more validation constraints  
# TODO: Create a GET endpoint at "/items/search/"
# TODO: Add parameter: q: str = Query(min_length=3, max_length=50, description="Search query")
# TODO: Add parameter: limit: int = Query(10, ge=1, le=100, description="Maximum number of items")
# TODO: Return: {"query": q, "limit": limit, "results": [...]}
# Hint: ge=1 means "greater than or equal to 1"
@app.get("/items/search/")
async def search_items(q: str = Query(min_length=3, max_length=50, description='Search query'),
                                     limit: int= Query(10, ge=1, le=100, description="Maximum number of items")):
                items = [x for x in fake_items_db if q in x["item_name"]]
                return items[:limit]
