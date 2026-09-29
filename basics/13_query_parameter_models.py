# Query Parameter Models
# Group query parameters into a Pydantic model (FastAPI 0.115+)

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

# TODO: Create a Pydantic model called "FilterParams" with:
# 1. model_config = {"extra": "forbid"}  (rejects unknown query params)
# 2. limit: int = 10 (default 10, max results to return)
# 3. offset: int = 0 (default 0, skip first N results)
# 4. order_by: str = "created_at" (default sort field)
class FilterParams(BaseModel):
    model_config: dict = {"extra": "forbid"}
    limit: int = 10
    offset: int = 0
    order_by: str = "created_at"

# TODO: Create a GET endpoint at "/items/" that:
# 1. Accepts filter_query: FilterParams = Query()
# 2. Returns {"filters": filter_query.model_dump()}
#
# Hint: Annotate with Query() to tell FastAPI these come from query string
@app.get("/items/")
async def get_items(filter_query: FilterParams=Query()):
                return {"filters": filter_query.model_dump()}