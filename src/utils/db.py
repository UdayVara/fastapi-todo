from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.utils.config import Settings

Base = declarative_base()
engine = create_engine(Settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





