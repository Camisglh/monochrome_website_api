from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreateSchema


def get_category(db: Session):
    return db.query(Category).all()


def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def create_category(db: Session, category: CategoryCreateSchema):
    _category = Category(name=category.name)
    db.add(_category)
    db.commit()
    db.refresh(_category)
    return _category
