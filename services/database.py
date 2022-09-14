import sqlalchemy as sql
from sqlalchemy.ext import declarative
from sqlalchemy import orm

SQLALCHEMY_DATABASE_URL = "sqlite:///../db/db.sqlite3"

engine = sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    return Base.metadata.create_all(bind=engine)
