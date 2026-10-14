from datetime import datetime, timedelta, timezone
from typing import Union

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
from typing_extensions import Annotated

# The key that signs every token. In a real app it comes from the environment,
# never from the code. Make one with: openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# johndoe's password is "secret". Only its bcrypt hash is stored.
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# ---------------------------------------------------------------------------
# Already done: the same models and helpers as the previous lesson.
# ---------------------------------------------------------------------------

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        return UserInDB(**db[username])


# ---------------------------------------------------------------------------
# Your part. Work through the TODOs in order: each one uses the ones before it.
# ---------------------------------------------------------------------------

class Token(BaseModel):
    # TODO 1: two fields, both str: access_token and token_type
    access_token: str
    token_type: str


# TODO 2: a CryptContext that uses bcrypt:
#   CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    # TODO 3: return pwd_context.verify(plain_password, hashed_password)
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db, username: str, password: str):
    # TODO 4: find the user with get_user. If there is none, or
    # verify_password says the password is wrong, return False.
    # Otherwise return the user.
    user = get_user(db, username)

    if not user or not verify_password(password, user.hashed_password):
        return False
    
    return user


def create_access_token(data: dict, expires_delta: timedelta):
    # TODO 5: copy `data`, add an "exp" key set to
    # datetime.now(timezone.utc) + expires_delta, and return
    # jwt.encode(that_dict, SECRET_KEY, algorithm=ALGORITHM).
    access_data = data.copy()
    access_data["exp"] = datetime.now(timezone.utc) + expires_delta
    return jwt.encode(access_data, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # TODO 6: decode the token with
    #   jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    # and read the username from its "sub" key. Raise credentials_exception
    # if decoding raises InvalidTokenError, if there is no "sub", or if
    # get_user finds nobody by that name. Otherwise return the user.
    try:
        access_data = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        username = access_data.get("sub")
        if not username:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username)
    if not user:
        raise credentials_exception
    return user

# Already done, as in the previous lesson.
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    # TODO 7: check form_data.username and form_data.password with
    # authenticate_user. If that returns False, raise an HTTPException with
    # status 401, detail "Incorrect username or password" and the header
    # {"WWW-Authenticate": "Bearer"}. Otherwise create a token for
    # {"sub": user.username} that expires in ACCESS_TOKEN_EXPIRE_MINUTES and
    # return Token(access_token=..., token_type="bearer").
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_data = {
        "sub": user.username
    }
    token = create_access_token(access_data, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return Token(access_token=token, token_type="bearer")


# TODO 8: the user from get_current_active_user is a UserInDB, so returning it
# as it is sends hashed_password to the client. Add response_model=User to
# the decorator below so only User's fields go out.
@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    # TODO 9: return [{"item_id": "Foo", "owner": <the current user's username>}]
    return [
        {
            "item_id": "Foo",
            "owner": current_user.username
        }
    ]
