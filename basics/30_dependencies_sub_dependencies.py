from typing import Annotated

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


# TODO: Create the first dependency (query_extractor)
# This should extract an optional query parameter 'q' and return it
def query_extractor(q: str | None = None):
    # TODO: Return the q parameter
    return q


# TODO: Create the second dependency (query_or_cookie_extractor) 
# This should depend on query_extractor and also check for a last_query cookie
# Parameters: q: Annotated[str, Depends(query_extractor)], last_query: Annotated[str | None, Cookie()] = None
def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    # TODO: If not q, return last_query, otherwise return q
    return q if q else last_query


# TODO: Create a GET /items/ path operation 
# Use query_or_cookie_extractor as dependency
# Parameter: query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
# Return: {"q_or_cookie": query_or_default}
@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    # TODO: Return dict with q_or_cookie key
    return {
        "q_or_cookie": query_or_default
    }