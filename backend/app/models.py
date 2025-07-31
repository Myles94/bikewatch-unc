from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TheftReport(BaseModel):
    user_id: str
    location_long: float
    location_lat: float
    vehicle_type: str
    description: str
    photo_url: Optional[str]
    date_of_theft: datetime

class Sighting(BaseModel):
    related_theft_report_id: str
    user_id: str 
    description: str
    photo_url: Optional[str]
    location_lat: float
    location_long: float
    date_of_sighting: datetime

class Feedback(BaseModel):
    user_id: str
    feedback_type: str
    content: str
    submitted_at: datetime

class Users(BaseModel):
    user_id: str
    name: str
    email: str
    role: str






