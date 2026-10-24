from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# TODO: Create origins list following the official FastAPI pattern
# Use: origins = ["http://localhost.tiangolo.com", "https://localhost.tiangolo.com", "http://localhost", "http://localhost:8080"]
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com", "http://localhost", "http://localhost:8080"
]

# TODO: Configure CORS middleware with appropriate settings
# Use app.add_middleware() with CORSMiddleware
# Set allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Item(BaseModel):
    name: str
    description: Optional[str] = None

items = []

# TODO: Create root endpoint that returns {"message": "Hello World"}
# Use function name: main() (following official docs)
@app.get("/")
async def root_here():
    return {"message": "Hello World"}

# TODO: Create GET /items/ endpoint to return all items
@app.get("/items/")
async def get_items():
    return items

# TODO: Create POST /items/ endpoint to add new items
@app.post("/items/")
async def create_items(item: Item):
    item_id = "item_{}".format(len(items) + 1)
    item_log = {
        "name": item.name,
    }
    if item.description:
        item_log["description"] = item.description
    items.append(item_log)
    return item_log