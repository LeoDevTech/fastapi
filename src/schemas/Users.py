from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_superuser: bool
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True
