from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Annotated

app = FastAPI()

# Pydantic model
class Item(BaseModel):
    name: str
    price: float

# Simple in-memory database
items_db: Dict[int, Item] = {}
next_id = 1

# Simulated database session class (like in real applications)
class DBSession:
    def __init__(self):
        self.connected = True
        self.transaction_count = 0
        print("Database connection established")
    
    def close(self):
        self.connected = False
        print("Database connection closed")

# TODO: Create a database session dependency with yield
# Follow the official FastAPI pattern from the docs:
# 
# async def get_db():
#     db = DBSession()
#     try:
#         yield db
#     finally:
#         db.close()
#
# This ensures the database session is always closed after the request

async def get_db():
    # TODO: Implement the database session dependency with yield
    # 1. Create a DBSession instance
    # 2. Use try/yield/finally pattern
    # 3. Yield the session for injection
    # 4. Close the session in finally block
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
    

# TODO: Create endpoints that use the database dependency

# POST /items/ - Create a new item
# - Use: item: Item, db: Annotated[DBSession, Depends(get_db)]
# - Increment db.transaction_count
# - Store item in items_db with next_id
# - Return: {"id": item_id, "name": item.name, "price": item.price,
#            "message": "Item created with database session cleanup"}
@app.post("/items/")
async def create_items(item: Item, db: Annotated[DBSession, Depends(get_db)]):
    global next_id
    db.transaction_count+=1
    items_db[next_id]=item
    item_detail = {
        "id": next_id,
        "name": item.name,
        "price": item.price,
        "message": "Item created with database session cleanup"
    }
    next_id+=1
    return item_detail

# GET /items/ - Get all items
# - Use: db: Annotated[DBSession, Depends(get_db)]
# - Increment db.transaction_count  
# - Return one dict per stored item:
#   [{"id": item_id, "name": item.name, "price": item.price}, ...]
@app.get("/items/")
async def get_items(db: Annotated[DBSession, Depends(get_db)]):
    db.transaction_count+=1
    results = [{"id": item_id, "name": item.name, "price": item.price} for item_id, item in items_db.items()]
    return results


print("🚀 Ready to implement dependencies with yield!")
print("💡 The DBSession class is provided - focus on the yield pattern!")