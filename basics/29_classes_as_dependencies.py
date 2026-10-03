from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# TODO: Create a CommonQueryParams class with __init__ method
# that takes: q (str | None = None), skip (int = 0), limit (int = 100)
# Store these as self.q, self.skip, self.limit
class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        # TODO: Store the parameters as instance attributes
        self.q = q
        self.skip = skip
        self.limit = limit

# TODO: Create GET /items/ endpoint using CommonQueryParams as dependency
# Use shortcut syntax: commons: Annotated[CommonQueryParams, Depends()]
# Return response dict with q (if provided) and sliced fake_items_db

@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    # TODO: Create response dict, add q if provided, slice fake_items_db
    result = {
        "items": fake_items_db[commons.skip:commons.limit+1]
    }
    if commons.q:
        result["q"] = commons.q
    return result

# TODO: Create GET /users/ endpoint using explicit dependency syntax
# Use: commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
# Return same structure but with "items" key

@app.get("/users/")
async def read_users(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    # TODO: Create response dict, add q if provided, slice fake_items_db
    result = {
        "items": fake_items_db[commons.skip:commons.limit+1]
    }
    if commons.q:
        result["q"] = commons.q
    return result