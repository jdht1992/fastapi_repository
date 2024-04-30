from fastapi import APIRouter
from router.v1.region import router

router_region = APIRouter(
    prefix="/api/v1"
)

router_region.include_router(router)
# router.include_router(city.router)

