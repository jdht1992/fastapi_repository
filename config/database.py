from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import get_settings


settings = get_settings()

DB_URL = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@localhost:5436/{settings.DB_NAME}"


engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Create a database session.
    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
