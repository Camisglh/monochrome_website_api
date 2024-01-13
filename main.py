from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def index(db: Session = Depends(get_db)):
    return {"message": "Hello World"}
