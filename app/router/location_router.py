from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import LocationCreateSchema
from app.crud.location_crud import *

location_router = APIRouter()


@location_router.post("/")
async def create_location_endpoint(
    location: LocationCreateSchema = Depends(),
    db: Session = Depends(get_db),
    image: UploadFile = File(...),
):
    _location = create_location(db, location, image)
    return _location


@location_router.get("/")
async def get_locations_endpoint(db: Session = Depends(get_db)):
    locations = get_location(db)
    return locations


@location_router.get("/{location_id}")
async def get_location_id_endpoint(location_id: int, db: Session = Depends(get_db)):
    location = get_location_id(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@location_router.put("/{location_id}")
async def update_location_id_endpoint(
    location_id: int,
    location: LocationCreateSchema = Depends(),
    db: Session = Depends(get_db),
    image: UploadFile = File(...),
):
    _location = update_location(db, location_id, location)
    if not _location:
        raise HTTPException(status_code=404, detail="Location not found")
    return _location
