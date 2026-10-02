# Request Forms
# Learn how to receive form data instead of JSON

from fastapi import FastAPI, Form

app = FastAPI()

# TODO: Import Form from fastapi
# Hint: from fastapi import FastAPI, Form

# TODO: Create a POST endpoint at "/login/" that:
# 1. Accepts "username" and "password" as form fields (not JSON)
# 2. Returns {"username": username}
# 
# Hint: Use Form() as the default value for parameters
# Example: username: str = Form(), password: str = Form()

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
