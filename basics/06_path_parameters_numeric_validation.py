# Path Parameters and Numeric Validations - Following Official FastAPI Tutorial
# Learn how to add validation constraints to path parameters

from fastapi import FastAPI, Path, Query
# TODO: Import Path and Query from fastapi

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Step 1: Add validation to path parameters
# TODO: Create a GET endpoint at "/items/{item_id}"
# TODO: Add parameter: item_id: int = Path(ge=1)
# TODO: Return: {"item_id": item_id}
# Hint: Path(ge=1) means the item_id must be greater than or equal to 1
@app.get("/items/{item_id}")
async def get_item(item_id: int = Path(ge=1)):
                return {"item_id": item_id}

# Step 2: Combine Path and Query validations
# TODO: Create a GET endpoint at "/items/{item_id}/details"
# TODO: Add parameter: item_id: int = Path(ge=1, le=1000, description="The ID of the item")
# TODO: Add parameter: q: str | None = Query(default=None, max_length=50)
# TODO: Return: {"item_id": item_id, "q": q, "details": "Item details here"}
@app.get("/items/{item_id}/details")
async def get_item_detail(item_id: int = Path(ge=1, le=1000, descript="The ID of the item"),
                                    q: str|None = Query(default=None, max_length=50)):
            return {"item_id": item_id, "q": q, "details": "Item details here"}

# Step 3: Add metadata to path parameters
# TODO: Create a GET endpoint at "/users/{user_id}"
# TODO: Add parameter: user_id: int = Path(title="User ID", description="The ID of the user to get", ge=1)
# TODO: Return: {"user_id": user_id, "message": f"User {user_id} profile"}
@app.get("/users/{user_id}")
async def get_user_id(user_id: int = Path(title='User ID', description='The ID of the user to get', ge=1)):
                return  {"user_id": user_id, "message": f"User {user_id} profile"}
