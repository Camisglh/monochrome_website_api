from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.models import Location
from app.schemas import LocationCreateSchema


def save_image(upload_file: UploadFile):
    with open(f"app/images/{upload_file.filename}", "wb") as f:
        f.write(upload_file.file.read())


def create_location(db: Session, location: LocationCreateSchema, image: UploadFile):
    _location = Location(name=location.name, description=location.description)

    if image:
        save_image(image)
    _location.image = f"images/{image.filename}"

    db.add(_location)
    db.commit()
    db.refresh(_location)
    return _location
