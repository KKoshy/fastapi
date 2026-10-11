from typing import Union, Optional
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: Create a User model using Pydantic
# Follow the official FastAPI pattern:
# class User(BaseModel):
#     username: str
#     email: Union[str, None] = None
#     full_name: Union[str, None] = None
#     disabled: Union[bool, None] = None

class User(BaseModel):
    # TODO: Add the user fields following the official pattern above
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

# TODO: Create a fake_decode_token function
# Follow the official pattern:
# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", 
#         email="john@example.com", 
#         full_name="John Doe"
#     )

def fake_decode_token(token):
    # TODO: Return a User instance with decoded token data
    return User(
        username=token + "fakedecoded",
        email="john@example.com",
        full_name="John Doe"
    )

# TODO: Create get_current_user dependency
# Follow the official pattern:
# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     user = fake_decode_token(token)
#     return user
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
                user=fake_decode_token(token)
                return user

# TODO: Create /users/me endpoint
# Follow the official pattern:
# @app.get("/users/me")
# async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
#     return current_user
@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
                return current_user