from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app.models import Base
from app.router.router import main_router
from app.middleware.password_check_middleware import PasswordCheckMiddleware
from app.middleware.error_check_middleware import ErrorCheckMiddleware
from app.middleware.validate_middleware import ValidateMiddleware
from app.middleware.crud_check_middleware import CRUDMiddleware

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(PasswordCheckMiddleware)

app.add_middleware(ErrorCheckMiddleware)

app.add_middleware(ValidateMiddleware)

app.add_middleware(CRUDMiddleware)

# add router
app.include_router(main_router, prefix="/api")
