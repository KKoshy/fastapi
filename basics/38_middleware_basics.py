import time
from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None


# Sample data
items = {
    "foo": {"name": "The Foo Wrestlers"},
    "bar": {"name": "The Bar Tenders"}
}


# TODO: Create a middleware that adds a custom header "X-Process-Time" 
# containing the time in seconds it took to process the request
# Use the @app.middleware("http") decorator
# Hint: Use time.perf_counter() for precise timing
@app.middleware("http")
async def calculate_process_time(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id in items:
        return items[item_id]
    return {"error": "Item not found"}


# TODO: Add a POST endpoint that creates a new item
# This will help demonstrate middleware working with different HTTP methods
@app.post("/items/")
async def create_item(item: Item):
    items[item.name] = {
        "name": item.name,
        "id": "item_{}".format(len(items) + 1)
    }
    if item.description:
        items[item.name]["description"] = item.description
    return items[item.name]