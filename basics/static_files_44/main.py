from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# TODO: Import StaticFiles from fastapi.staticfiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="basics/static_files_44/static"), name="static")

# TODO: Mount the static files directory
# Use app.mount() to serve files from the "static" directory at the "/static" path
# Hint: app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    # TODO: Return information about the static files demo
    # Include links to the static demo page:
    # {"message": "FastAPI Static Files Demo", "docs": "/docs", "static_demo": "/static/index.html"}
    return {"message": "FastAPI Static Files Demo", "docs": "/docs", "static_demo": "/static/index.html"}