# Body - Nested Models
# Learn to create complex nested data structures with FastAPI and Pydantic

from typing import Dict, List, Set, Union
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# TODO 1: Create the Image nested model
# Fields: url (HttpUrl), name (str)
class Image(BaseModel):
    # TODO: Add the fields
    url: HttpUrl
    name: str

# TODO 2: Create the Item model with nested structures
# Fields:
# - name: str
# - description: Union[str, None] = None
# - price: float
# - tax: Union[float, None] = None
# - tags: Set[str] = set()  # Set of unique strings
# - image: Union[Image, None] = None  # Single nested model
class Item(BaseModel):
    # TODO: Add the fields with proper types
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[Image, None] = None

# TODO 3: Create ItemWithImages model for lists of nested models
# Same as Item but with:
# - images: List[Image] = []  # List of nested models instead of single image
class ItemWithImages(BaseModel):
    # TODO: Add the fields
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    images: List[Image] = []

# TODO 4: Create endpoints
# 1. PUT /items/{item_id} - update_item(item_id: int, item: Item)
@app.put("/items/{item_id}")
async def update_item(item_id: int, *, item: Item):
          return {"item_id": item_id, "item": item}

# 2. PUT /items/{item_id}/images - update_item_with_images(item_id: int, item: ItemWithImages)
@app.put("/items/{item_id}/images")
async def update_item_with_images(item_id: int, *, item: ItemWithImages):
                return {"item_id": item_id, "item": item}

# 3. POST /index-weights/ - create_index_weights(weights: Dict[int, float])
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
                return weights
