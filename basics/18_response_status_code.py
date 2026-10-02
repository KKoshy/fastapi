# Response Status Code
# Learn how to specify HTTP status codes for your API responses

from fastapi import FastAPI, status

app = FastAPI()

# TODO: Create a POST endpoint at "/items/" that:
# 1. Accepts a "name" parameter as a query parameter (string)
# 2. Returns {"name": name}
# 3. Uses status code 201 (Created) instead of the default 200
# 
# Hint: Use the status_code parameter in the decorator
# Example: @app.post("/items/", status_code=???)
# For query parameters, just define: def create_item(name: str):
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

# TODO: Import and use FastAPI status constants for better readability
# Hint: from fastapi import status
# Then use: status.HTTP_201_CREATED
