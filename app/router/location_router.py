from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import LocationCreateSchema
from app.crud.location_crud import create_location

location_router = APIRouter()


@location_router.post("/")
async def create_location_endpoint(
    location: LocationCreateSchema = Depends(),
    db: Session = Depends(get_db),
    image: UploadFile = File(...),
):
    """
    Create a new location with an optional image.

    :param location: Location data.
    :param db: Database session.
    :param image: Optional image file.

    :return: Created location.
    """
    _location = create_location(db, location, image)
    return _location


#
