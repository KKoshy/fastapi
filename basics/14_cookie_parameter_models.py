# Cookie Parameter Models
# Group cookies into a Pydantic model (FastAPI 0.115+)

from fastapi import FastAPI, Cookie
from pydantic import BaseModel

app = FastAPI()

# TODO: Create a Pydantic model called "UserPreferences" with:
# 1. theme: str = "light"
# 2. font_size: int = 14
# 3. language: str = "en"
class UserPreferences(BaseModel):
    theme: str = "light"
    font_size: int = 14
    language: str = "en" 

# TODO: Create a GET endpoint at "/preferences/" that:
# 1. Accepts prefs: UserPreferences = Cookie()
# 2. Returns {"preferences": prefs.model_dump()}
@app.get("/preferences/")
async def get_preferences(prefs: UserPreferences=Cookie()):
                return {"preferences": prefs.model_dump()}


# model_dump() — converts a Pydantic model to a Python dictionary.
# model_dump_json() — converts a Pydantic model to a JSON string.
# dict() — the older Pydantic v1 method; in Pydantic v2, use model_dump().

