from sqlalchemy import create_engine, false, ForeignKey  # type: ignore
# from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, \
    mapped_column  # type: ignore

from config import settings

# sqlalchemy_database_url = "postgresql+psycopg://postgres:jadzia01@localhost/fastapi"
sqlalchemy_database_url = (
    f"postgresql+psycopg://{settings.database_username}:"
    f"{settings.database_password}@"f"{settings.database_hostname}:"
    f"{settings.database_port}/{settings.database_name}")

engine = create_engine(sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
