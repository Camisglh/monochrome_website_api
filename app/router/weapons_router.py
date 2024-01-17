from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import WeaponsCreateSchema
from app.crud.weapons_crud import *

weapons_router = APIRouter()


@weapons_router.post("/")
async def create_weapons_endpoint(
    weapons: WeaponsCreateSchema = Depends(),
    db: Session = Depends(get_db),
    image: UploadFile = File(...),
):
    _weapons = create_rewards(db, weapons, image)
    return _weapons


@weapons_router.get("/")
async def get_weapons_endpoint(db: Session = Depends(get_db)):
    weapons = get_weapons(db)
    return weapons


@weapons_router.get("/{weapons_id}")
async def get_weapons_id_endpoint(weapons_id: int, db: Session = Depends(get_db)):
    weapons = get_weapons_id(db, weapons_id)
    if not weapons:
        raise HTTPException(status_code=404, detail="Weapons not found")
    return weapons


@weapons_router.put("/{weapons_id}")
async def update_weapons_id_endpoint(
    weapons_id: int,
    weapons: WeaponsCreateSchema = Depends(),
    db: Session = Depends(get_db),
    image: UploadFile = File(...),
):
    _weapons = update_weapons(db, weapons_id, weapons)
    if not _weapons:
        raise HTTPException(status_code=404, detail="Weapons not found")
    return _weapons


@weapons_router.delete("/{weapons_id}")
async def delete_weapons_id_endpoint(weapons_id: int, db: Session = Depends(get_db)):
    _weapons = delete_weapons(db, weapons_id)
    if not _weapons:
        raise HTTPException(status_code=404, detail="Weapons not found")
    return _weapons
