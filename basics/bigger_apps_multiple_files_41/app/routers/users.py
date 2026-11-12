# TODO: Import APIRouter from FastAPI
from fastapi import APIRouter


# TODO: Create an APIRouter instance
router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
    ) # TODO: Uncomment after importing get_token_header)


# TODO: Create a GET endpoint for "/users/" with tags=["users"]
# It should return a list of users: [{"username": "Rick"}, {"username": "Morty"}]
@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


# TODO: Create a GET endpoint for "/users/me" with tags=["users"]
# It should return the current user: {"username": "fakecurrentuser"}
@router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


# TODO: Create a GET endpoint for "/users/{username}" with tags=["users"]
# It should accept a username parameter and return: {"username": username}
@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}
