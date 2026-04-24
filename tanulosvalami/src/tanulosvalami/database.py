"""
Database configuration and session management.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLite database URL
# A '///' után 3 slash = relatív path, 4 slash = abszolút path
DATABASE_URL = "sqlite:///./feedback.db"

# Engine létrehozása
# check_same_thread=False: szükséges SQLite-hoz FastAPI-val
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True  # SQL query-k kiírása (fejlesztéshez hasznos)
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Declarative Base - minden model ebből fog örökölni
class Base(DeclarativeBase):
    """Base class for all database models."""
    pass


def get_db():
    """
    Dependency injection helper for FastAPI.
    Létrehoz egy DB session-t és bezárja használat után.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()