# Header Parameters
# Learn to read and validate HTTP headers

from fastapi import FastAPI, Header

app = FastAPI()

# TODO: Import Header from fastapi
# Hint: from fastapi import FastAPI, Header

# TODO: Create a GET endpoint at "/headers/info/" that:
# 1. Reads the "User-Agent" header (optional, default None)
# 2. Reads the "Accept-Language" header (optional, default "en")
# 3. Returns {"user_agent": user_agent, "accept_language": accept_language}
#
# Note: Hyphens in header names become underscores in Python
# "User-Agent" -> user_agent, "Accept-Language" -> accept_language
# Example: user_agent: str | None = Header(default=None)
@app.get("/headers/info/")
async def get_info(user_agent:str|None=Header(default=None), accept_language:str|None=Header(default="en")):
                return {"user_agent": user_agent, "accept_language": accept_language}

# TODO: Create a GET endpoint at "/secure/data/" that:
# 1. Reads a required "X-Token" header
# 2. Reads an optional "X-Request-Id" header (default None)
# 3. Returns {"data": "secret", "token": x_token, "request_id": x_request_id}
@app.get("/secure/data/")
async def get_security_data(x_token: str=Header(), x_request_id:str|None = Header(default=None)):
                return {"data": "secret", "token": x_token, "request_id": x_request_id}
