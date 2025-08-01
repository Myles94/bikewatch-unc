from fastapi import APIRouter, HTTPException
from ..models import TheftReport
from ..database import supabase
from postgrest.exceptions import APIError  # <-- Add this import

router = APIRouter()

@router.post("/reports")
def create_report(report: TheftReport):
    data = report.dict()
    data['date_of_theft'] = data['date_of_theft'].isoformat()
    
    try:
        response = supabase.table("theft_reports").insert(data).execute()
        return response.data
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/reports")
def list_reports():
    try:
        response = supabase.table("theft_reports").select("*").order("date_of_theft", desc=True).execute()
        return response.data
    except APIError as e:
        raise HTTPException(status_code=500, detail=str(e))

