# import models
from database import engine, SessionLocal, get_db
import time
from fastapi import FastAPI, Response, status, HTTPException, Request
import psycopg  # type: ignore
from routers import ikv
from psycopg.rows import dict_row
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import logging.config
import json
import os

os.makedirs("/var/log/my_app", exist_ok=True)

# models.Base.metadata.create_all(bind=engine) #Nodig wanneer je geen Alembic
# maar alleen SQLAlchemy gebruikt

with open("log_config.json", "r") as f:
    config = json.load(f)

logging.config.dictConfig(config)

app = FastAPI(
    title="UWV Datawarehouse API voor FDS Digilab casus november 2025",
    description="Contact: manolo.schotsborg@uwv.nl",
    version="0.0.1",
    openapi_url="/api/v0/openapi.json",
    docs_url="/api/v0/docs",
    redoc_url="/api/v0/redoc",
)

# origins: list[str] = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

DISALLOWED_METHODS = {"PROPFIND", "ACL", "MKCALENDAR", "LINK", "BREW", "WHEN"}


@app.middleware("http")
async def add_version_header(request: Request, call_next):
    if request.method.upper() in DISALLOWED_METHODS:
        return PlainTextResponse("Method Not Allowed", status_code=405)

    response: Response = await call_next(request)

    if request.url.path.startswith("/api/v0"):
        response.headers["API-Version"] = "0.0.1"
    elif request.url.path.startswith("/api/v1"):
        response.headers["API-Version"] = "1.0.0"
    return response


while True:
    try:
        conn = psycopg.connect(
            host=f"{settings.database_hostname}",
            dbname=f"{settings.database_name}",
            user=f"{settings.database_username}",
            password=f"{settings.database_password}",
            row_factory=dict_row,
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as e:
        print("Connection to database failed")
        print("Error: ", e)
        time.sleep(2)

app.include_router(ikv.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello World"}
