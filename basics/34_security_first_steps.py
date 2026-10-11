from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated

app = FastAPI()

# TODO: Create OAuth2PasswordBearer instance
# Follow the official FastAPI pattern:
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: Create a protected endpoint that uses OAuth2 security
# Follow this pattern from the official docs:
#
# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}
#
# This will automatically:
# - Require Authorization header with Bearer token
# - Show "Authorize" button in FastAPI docs
# - Return 401 if no token provided

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    # TODO: Add the token parameter with proper typing
    # Use: token: Annotated[str, Depends(oauth2_scheme)]
    # Return: {"token": token}
    return {"token": token}
