from datetime import datetime
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


app = FastAPI()


@app.put("/items/{id}")
async def update_item(id: str, item: Item):
    # TODO: Use jsonable_encoder to convert the Pydantic model to JSON-compatible format
    # TODO: Store the encoded item data in fake_db with the id as key
    # TODO: Return the encoded data to show it's working
    # Hint: json_compatible_item_data = jsonable_encoder(item)
    # Hint: fake_db[id] = json_compatible_item_data
    # Hint: return json_compatible_item_data
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return json_compatible_item_data