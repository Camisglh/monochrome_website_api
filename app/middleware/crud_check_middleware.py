from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


class CRUDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method not in {"GET", "POST", "PUT", "DELETE"}:
            raise HTTPException(status_code=405, detail="Method Not Allowed")
        return await call_next(request)
