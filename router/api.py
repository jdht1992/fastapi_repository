from fastapi import APIRouter
from router.v1.region import router_region
from router.v1.city import router_city

router_v1 = APIRouter(
    prefix="/api/v1"
)

router_v1.include_router(router_region)
router_v1.include_router(router_city)
