from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategorySchema


def get_category(db: Session):
    return db.query(Category).all()


def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def create_category(db: Session, category: CategorySchema):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category: CategorySchema):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db.query(Category).filter(Category.id == category_id).delete()
    db.commit()
