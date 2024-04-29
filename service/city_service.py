from typing import List
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from repository.city_repository import CityRepository
from repository.region_repository import RegionRepository
from schemas.city_schema import CityInput, CityOutput


class CityService:
    """
    Service class for handling cities.
    """
    def __init__(self, session: Session):
        self.city_repository = CityRepository(session)
        self.region_repository = RegionRepository(session)

    def create(self, data: CityInput) -> CityOutput:
        if self.city_repository.city_exists_by_name(data.name):
            raise HTTPException(status_code=400, detail="City already exists")
        
        if not self.region_repository.region_exists_by_id(data.region_id):
            raise HTTPException(status_code=400, detail="Region not found")
        
        region = self.region_repository.get_region(data.region_id)
        city = self.city_repository.create(data)
        return CityOutput(**city.model_dump(exclude_none=True), region=region)
    
    def get_all(self):
        return self.city_repository.get_all()

    def get_all_by_region(self, region_id: UUID4) -> List[CityOutput]:
        return self.city_repository.get_all_by_region(region_id)
    
    def update(self, _id: UUID4, data: CityInput):
        if not self.city_repository.city_exists_by_id(_id):
            raise HTTPException(status_code=404, detail="City not found")
        
        city = self.city_repository.get_by_id(_id)
        update_city = self.city_repository.update(city, data)

        return update_city
    
    def delete(self, _id: UUID4) -> bool:
        if not self.city_repository.city_exists_by_id(_id):
            raise HTTPException(status_code=404, detail="City not found")
        
        city = self.city_repository.get_by_id(_id)
        return self.city_repository.delete(city)
