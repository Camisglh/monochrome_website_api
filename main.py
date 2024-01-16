from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app.models import Base
from app.router.category_router import router
from app.router.ally_router import allyrouter
from app.router.enemy_router import enemyrouter
from app.router.location_router import location_router

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/category", tags=["category"])
app.include_router(allyrouter, prefix="/ally", tags=["ally"])
app.include_router(enemyrouter, prefix="/enemy", tags=["enemy"])
app.include_router(location_router, prefix="/location", tags=["location"])
