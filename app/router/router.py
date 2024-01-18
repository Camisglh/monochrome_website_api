from fastapi import APIRouter
from app.router.category_router import router
from app.router.ally_router import allyrouter
from app.router.enemy_router import enemyrouter
from app.router.location_router import location_router
from app.router.weapons_router import weapons_router
from app.router.charaster_router import charaster_router

main_router = APIRouter()

main_router.include_router(router, prefix="/category", tags=["category"])
main_router.include_router(allyrouter, prefix="/ally", tags=["ally"])
main_router.include_router(enemyrouter, prefix="/enemy", tags=["enemy"])
main_router.include_router(location_router, prefix="/location", tags=["location"])
main_router.include_router(weapons_router, prefix="/weapons", tags=["weapons"])
main_router.include_router(charaster_router, prefix="/charaster", tags=["charaster"])
