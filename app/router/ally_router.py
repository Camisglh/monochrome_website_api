from fastapi import APIRouter, HTTPException, Path, Depends
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from app.schemas import AllyCreateSchema
from app.crud.ally_crud import *

allyrouter = APIRouter()


@allyrouter.get("/")
async def get_all_allies(db: Session = Depends(get_db)):
    allies = get_ally(db)
    return allies


@allyrouter.post("/")
async def create(ally: AllyCreateSchema, db: Session = Depends(get_db)):
    _ally = create_ally(db, ally)
    return _ally


@allyrouter.get("/{ally_id}")
async def get_ally_id(ally_id: int, db: Session = Depends(get_db)):
    _ally = get_ally_by_id(db, ally_id)
    if not _ally:
        raise HTTPException(status_code=404, detail="Ally not found")
    return _ally


@allyrouter.put("/{ally_id}")
async def update_ally_id(
    ally_id: int, ally: AllyCreateSchema, db: Session = Depends(get_db)
):
    _ally = update_ally(db, ally_id, ally)
    if not _ally:
        raise HTTPException(status_code=404, detail="Ally not found")
    return _ally


@allyrouter.delete("/{ally_id}")
async def delete_ally_id(ally_id: int, db: Session = Depends(get_db)):
    _ally = remote_ally(db, ally_id)
    if not _ally:
        raise HTTPException(status_code=404, detail="Ally not found")
    return _ally
