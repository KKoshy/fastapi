# Header Parameter Models
# Group headers into a Pydantic model (FastAPI 0.115+)

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

# TODO: Create a Pydantic model called "CommonHeaders" with:
# 1. x_token: str (required API token)
# 2. x_request_id: str | None = None (optional request tracking)
# 3. accept_language: str = "en" (language preference)
#
# Note: header hyphens auto-convert to underscores
class CommonHeaders(BaseModel):
    x_token: str
    x_request_id: str | None = None
    accept_language: str = "en"

# TODO: Create a GET endpoint at "/info/" that:
# 1. Accepts headers: CommonHeaders = Header()
# 2. Returns {"headers": headers.model_dump()}
@app.get("/info/")
async def get_info(headers: CommonHeaders = Header()):
                return {"headers": headers.model_dump()} 