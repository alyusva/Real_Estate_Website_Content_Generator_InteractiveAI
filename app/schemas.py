from pydantic import BaseModel, Field
from typing import Optional

class Location(BaseModel):
    city: str
    neighborhood: str

class Features(BaseModel):
    bedrooms: int
    bathrooms: int
    area_sqm: float
    balcony: Optional[bool] = None
    parking: Optional[bool] = None
    elevator: Optional[bool] = None
    floor: Optional[int] = None
    year_built: Optional[int] = None

class PropertyInput(BaseModel):
    title: str
    location: Location
    features: Features
    price: float
    listing_type: str = Field(..., description="'sale' or 'rent'")
    language: str = Field("en", description="Language code: 'en' or 'pt'")

class ContentOutput(BaseModel):
    content: str 