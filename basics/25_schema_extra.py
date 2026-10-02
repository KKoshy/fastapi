# Schema Extra - Examples
# Provide example data for your API documentation

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# TODO: Create a Pydantic model called "Item" with:
# 1. name: str
# 2. description: str | None = None
# 3. price: float
# 4. tax: float | None = None
# 5. Add model_config with json_schema_extra containing an example:
#    model_config = {
#        "json_schema_extra": {
#            "examples": [
#                {
#                    "name": "Laptop",
#                    "description": "A powerful laptop",
#                    "price": 999.99,
#                    "tax": 89.99,
#                }
#            ]
#        }
#    }
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                   "name": "Laptop",
                   "description": "A powerful laptop",
                   "price": 999.99,
                   "tax": 89.99,
                }
            ]
        }
    }

# TODO: Create a POST endpoint at "/items/" that:
# 1. Accepts item: Item
# 2. Returns the item data as a dictionary"
@app.post("/items/")
async def create_items(item: Item):
    return item.model_dump()
