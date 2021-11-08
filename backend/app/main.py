from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables
from app.routers import auth
from app.routers import categories
from app.routers import items
from app.routers import orders
from app.routers import users
from app.settings import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(items.router)
app.include_router(orders.router)


@app.on_event("startup")
async def on_startup():
    create_db_and_tables()
    from .example_data import create_example_data

    create_example_data()
