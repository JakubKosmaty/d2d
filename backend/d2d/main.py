from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from d2d.database import create_db_and_tables
from d2d.routers import auth
from d2d.routers import categories
from d2d.routers import items
from d2d.routers import orders
from d2d.routers import users
from d2d.routers import codes
from d2d.settings import settings

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
app.include_router(codes.router)


@app.on_event("startup")
async def on_startup():
    create_db_and_tables()
    from .example_data import create_example_data

    create_example_data()
