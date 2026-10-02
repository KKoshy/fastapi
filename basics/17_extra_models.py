# Extra Models
# Learn to create multiple related models for different use cases

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str|None = None

# TODO: Create three user models:
# 1. UserIn - for input data (includes password)
class UserIn(UserBase):
    password: str

# 2. UserOut - for output data (excludes password)  
class UserOut(UserBase):
    pass

# 3. UserInDB - for database storage (includes hashed_password)
class UserInDB(UserBase):
    hashed_password: str


# TODO: Create a fake password hasher function
async def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

# TODO: Create a fake save user function that:
# - Takes a UserIn object
# - Hashes the password (remember to await the hasher!)
# - Creates a UserInDB object with the hashed password
# - Returns the UserInDB object
async def fake_save_user(user_in: UserIn):
      hashed_password = await fake_password_hasher(user_in.password)
      user_data = user_in.model_dump(exclude={"password"})
      user_in_db = UserInDB(**user_data, hashed_password=hashed_password)
      return user_in_db

# TODO: Create a POST endpoint at "/user/" that:
# - Accepts UserIn data
# - Uses response_model=UserOut to filter the response
# - Calls fake_save_user and returns the result (remember to await it!)
@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    return await fake_save_user(user_in)
