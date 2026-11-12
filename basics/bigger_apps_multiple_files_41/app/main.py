# TODO: Import the necessary modules
# Hint: You need FastAPI, Depends, and the modules we created
from fastapi import FastAPI, Depends

# TODO: Import dependencies from our dependencies module
# from .dependencies import get_query_token, get_token_header
from .dependencies import get_query_token, get_token_header

# TODO: Import routers from our routers package
# from .routers import items, users
from .routers import items, users

# TODO: Import admin router from internal package
# from .internal import admin
from .internal import admin

# TODO: Create FastAPI app with global dependencies
# Hint: Use dependencies=[Depends(get_query_token)] to apply to all routes
app = FastAPI(dependencies = [Depends(get_query_token)])

# TODO: Include the users router
# Hint: Use app.include_router(users.router)
app.include_router(users.router)

# TODO: Include the items router
# Hint: Use app.include_router(items.router)
app.include_router(items.router)

# TODO: Include the admin router with configuration
# Hint: Use prefix="/admin", tags=["admin"], dependencies=[Depends(get_token_header)], 
# and responses={418: {"description": "I'm a teapot"}}
app.include_router(admin.router,
                               prefix="/admin",
                               tags=["admin"],
                               dependencies=[Depends(get_token_header)],
                               responses={418: {"description": "I'm a teapot"}}
                               )

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
