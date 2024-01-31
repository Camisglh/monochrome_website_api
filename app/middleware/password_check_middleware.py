from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from dotenv import load_dotenv
import os


# Password verification for create update and delete operations.
class PasswordCheckMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_name="X-CRUD-Password"):
        self.header_name = header_name
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        load_dotenv()
        password = os.getenv("CRUD_PASSWORD")

        if request.method in ["POST", "PUT", "DELETE"]:
            request_password = request.headers.get(self.header_name)

            if not request_password or request_password != password:
                raise HTTPException(
                    status_code=403,
                    detail="Error: Incorrect password for operations CRUD",
                )

        response = await call_next(request)
        return response
