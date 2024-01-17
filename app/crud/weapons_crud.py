from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.models import Weapons
from app.schemas import WeaponsCreateSchema


def save_image(upload_file: UploadFile):
    with open(f"app/images/{upload_file.filename}", "wb") as f:
        f.write(upload_file.file.read())


def create_rewards(db: Session, weapons: WeaponsCreateSchema, image: UploadFile):
    _weapons = Weapons(name=weapons.name, description=weapons.description)

    if image:
        save_image(image)
    _weapons.image = f"images/{image.filename}"

    db.add(_weapons)
    db.commit()
    db.refresh(_weapons)
    return _weapons


def get_weapons_id(db: Session, weapons_id: int):
    return db.query(Weapons).filter(Weapons.id == weapons_id).first()


def get_weapons(db: Session):
    return db.query(Weapons).all()


def update_weapons(db: Session, weapons_id: int, weapons: WeaponsCreateSchema):
    _weapons = db.query(Weapons).filter(Weapons.id == weapons_id).first()
    _weapons.name = weapons.name
    _weapons.description = weapons.description
    db.commit()
    db.refresh(_weapons)
    return _weapons


def delete_weapons(db: Session, weapons_id: int):
    weapons = db.query(Weapons).filter(Weapons.id == weapons_id).first()
    if weapons:
        db.delete(weapons)
        db.commit()
        return weapons
    return None
