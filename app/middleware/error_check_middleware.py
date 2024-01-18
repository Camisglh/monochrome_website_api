from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
import logging


class ErrorCheckMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except SQLAlchemyError as e:
            logging.error(f"Database error: {e}")
            return JSONResponse(
                content={"detail": "An error occurred with the database operation."},
                status_code=500,
            )
        except HTTPException as http_exc:
            return JSONResponse(
                content={"detail": http_exc.detail}, status_code=http_exc.status_code
            )
        except Exception as exc:
            logging.error(f"Unhandled error: {exc}")
            return JSONResponse(
                content={"detail": "An internal server error occurred."},
                status_code=500,
            )
