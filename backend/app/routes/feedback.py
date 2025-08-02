from fastapi import APIRouter, HTTPException
from ..models import Feedback
from ..database import supabase
from postgrest.exceptions import APIError  # match the reports.py structure

router = APIRouter()

@router.post("/feedback")
def submit_feedback(feedback: Feedback):
    data = feedback.dict()
    data['submitted_at'] = data['submitted_at'].isoformat()  # serialize datetime

    try:
        response = supabase.table("feedback").insert(data).execute()
        return response.data
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/feedback")
def list_feedback():
    try:
        response = supabase.table("feedback").select("*").order("submitted_at", desc=True).execute()
        return response.data
    except APIError as e:
        raise HTTPException(status_code=500, detail=str(e))
