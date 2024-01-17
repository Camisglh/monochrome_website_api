from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.models import Charaster
from app.schemas import CharasterCreateSchema


def save_image(upload_file: UploadFile):
    with open(f"app/images/{upload_file.filename}", "wb") as f:
        f.write(upload_file.file.read())


def create_charaster(db: Session, charaster: CharasterCreateSchema, image: UploadFile):
    try:
        _charaster = Charaster(
            name=charaster.name,
            quote=charaster.quote,
            description=charaster.description,
            status=charaster.status,
            role=charaster.role,
            kills=charaster.kills,
            category=charaster.category or [],
            allies=charaster.allies or [],
            enemies=charaster.enemies or [],
        )

        if image:
            save_image(image)
            _charaster.image = f"images/{image.filename}"

        db.add(_charaster)
        db.commit()
        db.refresh(_charaster)
        return _charaster

    except Exception as e:
        # Запись ошибки в лог или вывод для отладки
        print(f"Ошибка при создании персонажа: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Внутренняя ошибка сервера")


def get_charaster(db: Session):
    return db.query(Charaster).all()


def get_charaster_id(db: Session, charaster_id: int):
    return db.query(Charaster).filter(Charaster.id == charaster_id).first()


def update_charaster(db: Session, charaster_id: int, charaster: CharasterCreateSchema):
    _charaster = db.query(Charaster).filter(Charaster.id == charaster_id).first()
    _charaster.name = charaster.name
    _charaster.quote = charaster.quote
    _charaster.description = charaster.description
    _charaster.status = charaster.status
    _charaster.role = charaster.role
    _charaster.kills = charaster.kills
    _charaster.category = charaster.category
    _charaster.allies = charaster.allies
    _charaster.enemies = charaster.enemies
    db.commit()
    db.refresh(_charaster)
    return _charaster


def delete_charaster(db: Session, charaster_id: int):
    charaster = db.query(Charaster).filter(Charaster.id == charaster_id).first()
    if charaster:
        db.delete(charaster)
        db.commit()
        return charaster
    return None
