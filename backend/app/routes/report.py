from fastapi import APIRouter, HTTPException

from models import TheftReport

from database import supabase

router = APIRouter()

@router.post("/reports")
def create_report(report: TheftReport):
    response = supabase.table("theft_reports").insert(report.dict()).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return response.data

@router.get("/reports")
def list_reports():
    response = supabase.table("theft_reports").select("*").order("date_of_theft", desc=True).execute()
    if response.error:
        raise HTTPException(status_code=500, detail=response.error.message)
    return response.data