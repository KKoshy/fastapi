from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    """Root endpoint returning a welcome message."""
    # TODO: Return a dictionary with key "msg" and value "Hello World"
    return {"msg": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Get an item by ID."""
    # TODO: Return a dictionary with "item_id" and "name" set to f"Item {item_id}"
    return {"item_id": item_id, "name": f"Item {item_id}"}
