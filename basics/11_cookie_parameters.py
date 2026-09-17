# Cookie Parameters
# Learn to read and validate HTTP cookies in your endpoints

from fastapi import FastAPI, Cookie

app = FastAPI()

# TODO: Import Cookie from fastapi
# Hint: from fastapi import FastAPI, Cookie

# TODO: Create a GET endpoint at "/user/settings/" that:
# 1. Reads a "session_id" cookie (required string)
# 2. Reads a "theme" cookie (optional, defaults to "light")
# 3. Reads a "language" cookie (optional, defaults to "en")
# 4. Returns {"session_id": session_id, "theme": theme, "language": language}
#
# Hint: Use Cookie() as the default value
# Example: session_id: str = Cookie(), theme: str = Cookie(default="light")
@app.get("/user/settings/")
async def get_user_settings(session_id: str = Cookie(), theme: str=Cookie(default="light"), language:str=Cookie(default="en")):
                return {"session_id": session_id, "theme": theme, "language": language}

# TODO: Create a GET endpoint at "/session/info/" that:
# 1. Reads the "session_id" cookie (required)
# 2. Returns {"session_id": session_id, "valid": True}
@app.get("/session/info/")
async def get_session_info(session_id: str = Cookie()):
                return {"session_id": session_id, "valid": True}
