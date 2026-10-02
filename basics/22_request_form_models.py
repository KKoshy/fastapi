# Request Form Models
# Group form fields into a Pydantic model (FastAPI 0.115+)
from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

# TODO: Create a Pydantic model called "RegistrationForm" with:
# 1. username: str (required)
# 2. email: str (required)
# 3. password: str (required)
# 4. full_name: str | None = None (optional)
class RegistrationForm(BaseModel):
    username: str
    email: str
    password: str
    full_name: str | None = None

# TODO: Create a POST endpoint at "/register/" that:
# 1. Accepts form_data: RegistrationForm = Form()
# 2. Returns {"message": "User registered", "username": form_data.username, "email": form_data.email}
@app.post("/register/")
async def register_user(form_data: RegistrationForm=Form()):
    return {
        "message": "User registered",
        "username": form_data.username,
        "email": form_data.email
    }