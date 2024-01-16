from fastapi import APIRouter, HTTPException, Path, Depends
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from app.schemas import EnemyCreateSchema
from app.crud.enemy_crud import *

enemyrouter = APIRouter()


@enemyrouter.get("/")
async def get_all_enemies(db: Session = Depends(get_db)):
    enemies = get_enemy(db)
    return enemies


@enemyrouter.post("/")
async def create(enemy: EnemyCreateSchema, db: Session = Depends(get_db)):
    _enemy = create_enemy(db, enemy)
    return _enemy


@enemyrouter.get("/{enemy_id}")
async def get_enemy_id(enemy_id: int, db: Session = Depends(get_db)):
    _enemy = get_enemy_by_id(db, enemy_id)
    if not _enemy:
        raise HTTPException(status_code=404, detail="Enemy not found")
    return _enemy


@enemyrouter.put("/{enemy_id}")
async def update_enemy_id(
    enemy_id: int, enemy: EnemyCreateSchema, db: Session = Depends(get_db)
):
    _enemy = update_enemy(db, enemy_id, enemy)
    if not _enemy:
        raise HTTPException(status_code=404, detail="Enemy not found")
    return _enemy


@enemyrouter.delete("/{enemy_id}")
async def delete_enemy_id(enemy_id: int, db: Session = Depends(get_db)):
    _enemy = remote_enemy(db, enemy_id)
    if not _enemy:
        raise HTTPException(status_code=404, detail="Enemy not found")
    return _enemy
