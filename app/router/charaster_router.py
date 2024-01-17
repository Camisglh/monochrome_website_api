from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CharasterCreateSchema
from app.crud.charaster_crud import *

charaster_router = APIRouter()


@charaster_router.post("/")
async def create_charaster_endpoint(
    charaster: CharasterCreateSchema = Depends(),
    db: Session = Depends(get_db),
    image: UploadFile = File(...),
):
    _charaster = create_charaster(db, charaster, image)
    return _charaster


@charaster_router.get("/")
async def get_charaster_endpoint(db: Session = Depends(get_db)):
    charaster = get_charaster(db)
    return charaster


@charaster_router.get("/{charaster_id}")
async def get_charaster_id_endpoint(charaster_id: int, db: Session = Depends(get_db)):
    charaster = get_charaster_id(db, charaster_id)
    if not charaster:
        raise HTTPException(status_code=404, detail="Charaster not found")
    return charaster


@charaster_router.put("/{charaster_id}")
async def update_charaster_id_endpoint(
    charaster_id: int,
    charaster: CharasterCreateSchema = Depends(),
    db: Session = Depends(get_db),
    image: UploadFile = File(...),
):
    _charaster = update_charaster(db, charaster_id, charaster)
    if not _charaster:
        raise HTTPException(status_code=404, detail="Charaster not found")
    return _charaster


@charaster_router.delete("/{charaster_id}")
async def delete_charaster_id_endpoint(
    charaster_id: int, db: Session = Depends(get_db)
):
    _charaster = delete_charaster(db, charaster_id)
    if not _charaster:
        raise HTTPException(status_code=404, detail="Charaster not found")
    return _charaster
