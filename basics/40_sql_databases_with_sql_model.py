from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager

# TODO: Create the Hero base model with shared fields (name, age)
# This model contains fields that are shared across other models
# Hint: Use Field(index=True) for name and age fields
class HeroBase(SQLModel):
    # Add name and age fields here
    name: str = Field(index=True)
    age: int = Field(default=None, index=True)

# TODO: Create the Hero table model with id and secret_name fields
# Remember to use table=True and proper Field configurations
# This is the actual database table model that inherits from HeroBase
class Hero(HeroBase, table=True):
    # Add id (primary key) and secret_name fields
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str

# TODO: Create the HeroPublic model for API responses (no secret_name)
# This model is returned to clients - excludes secret_name for security
# Hint: Inherit from HeroBase and add id field as required (int, not optional)
class HeroPublic(HeroBase):
    # Add id field
    id : int

# TODO: Create the HeroCreate model for creating heroes
# This model validates data from clients when creating heroes
# Hint: Inherit from HeroBase and add secret_name field
class HeroCreate(HeroBase):
    # Add secret_name field
    secret_name: str

# TODO: Create the HeroUpdate model with optional fields for updates
# All fields are optional for partial updates (use None defaults)
class HeroUpdate(SQLModel):
    # Add optional name, age, and secret_name fields
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None

# TODO: Set up the database engine with SQLite
# Use check_same_thread=False for FastAPI compatibility
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# TODO: Create connect_args dictionary and engine
# Hint: connect_args = {"check_same_thread": False}
# Replace with proper config
connect_args = {
    "check_same_thread": False
}
# Replace with create_engine call
engine = create_engine(sqlite_url)

# TODO: Create a function to create database tables
# Hint: Use SQLModel.metadata.create_all(engine)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# TODO: Create a session dependency using yield
# This ensures one session per request for thread safety
# Hint: Use 'with Session(engine) as session:' and yield the session
def get_session():
    with Session(engine) as session:
        yield session

# Create the dependency annotation
SessionDep = Annotated[Session, Depends(get_session)]

# TODO: Add startup event to create tables
# Hint: Call create_db_and_tables() function
# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


# replacing @app.on_event("startup") with lifespan since it is deprecated
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# TODO: Create endpoint to add a new hero
# Use HeroCreate for input validation and HeroPublic for response
# Hint: Use Hero.model_validate(hero) to convert HeroCreate to Hero
@app.post("/heroes/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

# TODO: Create endpoint to read heroes with pagination
# Use response_model=list[HeroPublic] and Query(le=100) for limit
# Hint: Use session.exec(select(Hero).offset(offset).limit(limit)).all()
@app.get("/heroes/", response_model=list[HeroPublic])
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    return session.exec(select(Hero).offset(offset).limit(limit)).all()

# TODO: Create endpoint to read a single hero by ID
# Use response_model=HeroPublic and check if hero exists
# Hint: Use session.get(Hero, hero_id) and raise 404 if not found
@app.get("/heroes/{hero_id}", response_model=HeroPublic)
def read_hero(hero_id: int, session: SessionDep):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero_db

# TODO: Create endpoint to update a hero
# Use PATCH for partial updates with HeroUpdate model
# Hint: Use hero.model_dump(exclude_unset=True) and hero_db.sqlmodel_update(hero_data)
@app.patch("/heroes/{hero_id}", response_model=HeroPublic)
def update_hero(hero_id: int, hero: HeroUpdate, session: SessionDep):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")

    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db

# TODO: Create endpoint to delete a hero
# Check if hero exists, then delete and return {"ok": True}
# Hint: Use session.get(), session.delete(), and session.commit()
@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    session.delete(hero_db)
    session.commit()
    return {"ok": True}