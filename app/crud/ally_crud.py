from sqlalchemy.orm import Session
from app.models import Ally
from app.schemas import AllyCreateSchema


def get_ally(db: Session):
    return db.query(Ally).all()


def get_ally_by_id(db: Session, ally_id: int):
    return db.query(Ally).filter(Ally.id == ally_id).first()


def create_ally(db: Session, ally: AllyCreateSchema):
    _ally = Ally(name=ally.name)
    db.add(_ally)
    db.commit()
    db.refresh(_ally)
    return _ally


def remote_ally(db: Session, ally_id: int):
    ally = db.query(Ally).filter(Ally.id == ally_id).first()
    if ally:
        db.delete(ally)
        db.commit()
        return ally
    return None


def update_ally(db: Session, ally_id: int, ally: AllyCreateSchema):
    _ally = db.query(Ally).filter(Ally.id == ally_id).first()
    _ally.name = ally.name
    db.commit()
    db.refresh(_ally)
    return _ally
