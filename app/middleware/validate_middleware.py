from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.schemas import (
    CategoryCreateSchema,
    AllyCreateSchema,
    EnemyCreateSchema,
    CharasterCreateSchema,
    LocationCreateSchema,
    WeaponsCreateSchema,
)


class ValidateMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method in ["POST", "PUT"]:
            try:
                data = await request.json()

                if "category" in data:
                    CategoryCreateSchema(**data["category"])
                if "allies" in data:
                    for ally_data in data["allies"]:
                        AllyCreateSchema(**ally_data)
                if "enemies" in data:
                    for enemy_data in data["enemies"]:
                        EnemyCreateSchema(**enemy_data)
                if "charaster" in data:
                    CharasterCreateSchema(**data["charaster"])
                if "location" in data:
                    LocationCreateSchema(**data["location"])
                if "weapons" in data:
                    WeaponsCreateSchema(**data["weapons"])
            except Exception as e:
                raise HTTPException(status_code=422, detail=f"ERROR: {str(e)}")

        response = await call_next(request)
        return response
