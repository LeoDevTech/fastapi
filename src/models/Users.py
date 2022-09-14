import uuid
from pydantic.datetime_parse import datetime
from sqlalchemy import Column, String, DateTime

from services.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, default=uuid.uuid4())
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(String, default=True)
    is_superuser = Column(String, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"User({self.email!r}, {self.first_name!r}, {self.last_name!r})"




