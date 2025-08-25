from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TheftReportCreate(BaseModel):
    location_long: float
    location_lat: float
    vehicle_type: str
    description: str
    photo_url: Optional[str] = None
    date_of_theft: datetime

class TheftReportDB(TheftReportCreate):
    id: str
    user_id: str
    mopderation_status: str
    created_at: datetime    #Pending, approved, rejected.

class SightingCreate(BaseModel):
    related_theft_report_id: Optional[str] = None
    description: str
    photo_url: Optional[str] = None
    location_lat: float
    location_long: float
    date_of_sighting: datetime

class SightingDB(SightingCreate):
    id: str
    user_id: str
    moderation_status: str
    created_at: datetime

class FeedbackCreate(BaseModel):
    feedback_type: str
    content: str

class FeedbackDB(FeedbackCreate):
    id: str
    user_id: Optional[str] = None
    submitted_at: datetime
    created_at: datetime
   

class Users(BaseModel):
    user_id: str
    name: str
    email: str
    role: str

class UserProfileDB(BaseModel):
    user_id: str        # == auth.users.id
    name: Optional[str] = None
    email: str
    role: str           # 'user' | 'admin'
    created_at: datetime






