from fastapi import APIRouter, HTTPException, Path, Depends
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from app.schemas import CategoryCreateSchema
from app.crud.category_crud import *

router = APIRouter()


@router.get("/")
async def get_all_categories(db: Session = Depends(get_db)):
    categories = get_category(db)
    return categories


@router.post("/")
async def create(category: CategoryCreateSchema, db: Session = Depends(get_db)):
    _category = create_category(db, category)
    return _category
