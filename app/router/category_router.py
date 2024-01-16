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


@router.get("/{category_id}")
async def get_category_id(category_id: int, db: Session = Depends(get_db)):
    _category = get_category_by_id(db, category_id)
    if not _category:
        raise HTTPException(status_code=404, detail="Category not found")
    return _category


@router.put("/{category_id}")
async def update_category_id(
    category_id: int, category: CategoryCreateSchema, db: Session = Depends(get_db)
):
    _category = update_category(db, category_id, category)
    if not _category:
        raise HTTPException(status_code=404, detail="Category not found")
    return _category


@router.delete("/{category_id}")
async def delete_category_id(category_id: int, db: Session = Depends(get_db)):
    _category = remote_category(db, category_id)
    if not _category:
        raise HTTPException(status_code=404, detail="Category not found")
    return _category
