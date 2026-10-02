from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Sample data (following official docs naming)
items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    # TODO: Check if item_id exists in items
    # If not found, raise HTTPException with status_code=404, detail="Item not found"
    # If found, return {"item": items[item_id]}
    try:
        return {"item": items[item_id]}
    except KeyError:
        raise HTTPException(status_code=404, detail='Item not found')


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    # TODO: Check if item_id exists in items
    # If not found, raise HTTPException with:
    #   - status_code=404
    #   - detail="Item not found" 
    #   - headers={"X-Error": "There goes my error"}
    # If found, return {"item": items[item_id]}
    try:
        return {"item": items[item_id]}
    except KeyError:
        raise HTTPException(status_code=404, detail='Item not found', 
        headers={"X-Error": "There goes my error"})


# TODO: Create a custom exception class called UnicornException
# It should accept a name parameter in __init__
class UnicornException(Exception):
    def __init__(self, name):
        self.name = name


# TODO: Add a custom exception handler for UnicornException
# Use @app.exception_handler(UnicornException)
# Return JSONResponse with status_code=418 and message about the unicorn
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
     )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    # TODO: If name == "yolo", raise UnicornException(name=name)
    # Otherwise return {"unicorn_name": name}
    if name=="yolo":
        raise UnicornException(name=name)
    return{"unicorn_name": name}