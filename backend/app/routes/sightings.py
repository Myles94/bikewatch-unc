from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from ..models import Sighting
from ..database import supabase
from postgrest.exceptions import APIError

router = APIRouter()

@router.post("/sightings")
def create_sighting(sighting: Sighting):
    data = sighting.dict()
    # Convert datetime to ISO string for JSON serialization
    data["date_of_sighting"] = sighting.date_of_sighting.isoformat()

    try:
        response = supabase.table("sightings").insert(data).execute()
        return response.data
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/sightings")
def get_sightings(related_report_id: Optional[str] = Query(None)):
    try:
        query = supabase.table("sightings").select("*")
        if related_report_id:
            query = query.eq("related_theft_report_id", related_report_id)
        response = query.execute()
        return response.data
    except APIError as e:
        raise HTTPException(status_code=500, detail=str(e))

