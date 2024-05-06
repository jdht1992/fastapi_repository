from config.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.region_schema import RegionInput, RegionOutput
from service.region_service import RegionService
from typing import List
from pydantic import UUID4


router_region = APIRouter(
    prefix="/location/region",
    tags=["location"]
)

@router_region.post("", status_code=201, response_model=RegionOutput)
def create_region(data: RegionInput, session: Session = Depends(get_db)):
    _service = RegionService(session)
    return _service.create(data)


@router_region.get("", status_code=200, response_model=List[RegionOutput])
def get_regions(session: Session = Depends(get_db)) -> List[RegionOutput]:
    _service = RegionService(session)
    return _service.get_all()


@router_region.put("/{_id}", status_code=200, response_model=RegionInput)
def update_region(_id: UUID4, data: RegionInput, session: Session = Depends(get_db)):
    _service = RegionService(session)
    return _service.update(_id, data)


@router_region.delete("/{_id}", status_code=204)
def delete_region(_id: UUID4, session: Session = Depends(get_db)):
    _service = RegionService(session)
    return _service.delete(_id)
