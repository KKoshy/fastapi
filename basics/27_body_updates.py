from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5

# Simulated database
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5}
}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    """Get an item by ID."""
    # TODO: Check if item exists, return 404 if not found
    # TODO: Return the item data
    try:
        return items[item_id]
    except KeyError:
        raise HTTPException(status_code=404, detail='Item not found')

@app.put("/items/{item_id}", response_model=Item)
async def update_item_with_put(item_id: str, item: Item):
    """Update an item completely (full replacement)."""
    # TODO: Check if item exists, return 404 if not found
    # TODO: Convert item to dict using jsonable_encoder and store in database
    # TODO: Return the encoded item
    data = jsonable_encoder(item)
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    items[item_id] = data
    return data

@app.patch("/items/{item_id}", response_model=Item)
async def update_item_with_patch(item_id: str, item: Item):
    """Update an item partially (only provided fields)."""
    # TODO: Check if item exists, return 404 if not found
    # TODO: Get stored item and convert to Pydantic model
    # TODO: Get only the fields that were set using item.dict(exclude_unset=True)
    # TODO: Create updated model using stored_item_model.copy(update=update_data)
    # TODO: Store updated item using jsonable_encoder and return the model
    data = jsonable_encoder(item)
    try:
        stored_data = items[item_id]
        stored_model = Item(**stored_data)
        updated_data = item.dict(exclude_unset=True)
        updated_item = stored_model.model_copy(update=updated_data)
        items[item_id] = jsonable_encoder(updated_item)
        return updated_item
    except KeyError:
        raise HTTPException(status_code=404, detail='Item not found')