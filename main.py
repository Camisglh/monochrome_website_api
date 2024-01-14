from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app.models import Base
from app.router.category_router import router

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/category", tags=["category"])
