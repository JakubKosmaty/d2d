from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import create_db_and_tables
from .routers import auth
from .routers import categories
from .routers import items
from .routers import orders
from .routers import users
from .settings import Settings

app = FastAPI(openapi_url=Settings.OPENAPI_URL)

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
