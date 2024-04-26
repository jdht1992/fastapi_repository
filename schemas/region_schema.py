from pydantic import BaseModel, Field, UUID4


class RegionInput(BaseModel):
    name: str = Field(min_length=1, max_length=120)


class RegionOutput(BaseModel):
    id: UUID4
    name: str
