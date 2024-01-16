from sqlalchemy.orm import Session
from app.models import Enemy
from app.schemas import EnemyCreateSchema


def get_enemy(db: Session):
    return db.query(Enemy).all()


def get_enemy_by_id(db: Session, enemy_id: int):
    return db.query(Enemy).filter(Enemy.id == enemy_id).first()


def create_enemy(db: Session, enemy: EnemyCreateSchema):
    _enemy = Enemy(name=enemy.name)
    db.add(_enemy)
    db.commit()
    db.refresh(_enemy)
    return _enemy


def remote_enemy(db: Session, enemy_id: int):
    enemy = db.query(Enemy).filter(Enemy.id == enemy_id).first()
    if enemy:
        db.delete(enemy)
        db.commit()
        return enemy
    return None


def update_enemy(db: Session, enemy_id: int, enemy: EnemyCreateSchema):
    _enemy = db.query(Enemy).filter(Enemy.id == enemy_id).first()
    _enemy.name = enemy.name
    db.commit()
    db.refresh(_enemy)
    return _enemy
