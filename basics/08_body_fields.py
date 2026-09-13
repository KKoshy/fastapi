# Body - Fields
# Learn to add validation and metadata to Pydantic model fields

from typing import Union
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# TODO: Create the Item model with Field validation
# Use Field() to add validation and metadata to model attributes:
# - name: str (no Field needed for simple required fields)
# - description: Union[str, None] with Field(default=None, title="The description of the item", max_length=300)
# - price: float with Field(gt=0, description="The price must be greater than zero")
# - tax: Union[float, None] = None (no Field needed)

class Item(BaseModel):
    # TODO: Add the fields with proper Field() validation
    name: str
    description: Union[str, None] = Field(default=None, title='The description of the item', max_length=300)
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

# TODO: Create the update_item endpoint
# - PUT /items/{item_id}
# - Parameters: item_id (int), item (Item = Body(embed=True))
# - Return: {"item_id": item_id, "item": item}
@app.put("/items/{item_id}")
async def update_item(item_id: int, *, item: Item=Body(embed=True)):
                return {"item_id": item_id, "item": item}
