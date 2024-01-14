from fastapi import APIRouter, HTTPException, Path, Depends
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from app.schemas import CategorySchema
from app.crud.category_crud import *

router = APIRouter()


@router.get("/")
async def get_all_categories(db: Session = Depends(get_db)):
    categories = get_category(db)
    return categories
