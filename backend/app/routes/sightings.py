from fastapi import APIRouter, HTTPException, Query
from ..models import Sighting
from ..database import supabase

router = APIRouter()

@router.post("/sightings")
def create_sighting(sighting: Sighting):
    response = supabase.table("sightings").insert(sighting.dict()).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return response.data

@router.get("/sightings")
def get_sightings(related_report_id: str = Query(...)):
    response = supabase.table("sightings").select("*").eq("related_theft_report_id", related_report_id).execute()
    if response.error:
        raise HTTPException(status_code=500, detail=response.error.message)
    return response.data