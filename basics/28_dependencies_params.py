from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI()

# TODO: Create a dependency function called 'common_parameters'
# It should accept: q (str | None = None), skip (int = 0), limit (int = 100)
# Return: {"q": q, "skip": skip, "limit": limit}

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    # TODO: Return a dictionary with the parameter values
    return {"q": q, "skip": skip, "limit": limit}


# TODO: Create GET /items/ endpoint that uses common_parameters as dependency
# Use: commons: Annotated[dict, Depends(common_parameters)]

@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    # TODO: Return the commons dictionary
    return commons


# TODO: Create GET /users/ endpoint that uses the same dependency pattern

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    # TODO: Return the commons dictionary
    return commons