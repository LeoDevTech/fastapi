from fastapi import FastAPI, Depends
from sqlalchemy import orm
from schemas.Users import UserCreate
from services.database import get_db, create_database

api = FastAPI(
    title="API",
    description="API demostrativa",
    version="0.0.1",
    docs_url="/",
    redoc_url=None,
)

create_database()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:api",
        host="127.0.0.1",
        port=9000,
        reload=True,
        debug=True,
        workers=2,
    )

