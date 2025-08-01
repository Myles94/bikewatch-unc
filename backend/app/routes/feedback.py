from fastapi import APIRouter, HTTPException
from ..models import Feedback
from ..database import supabase

router = APIRouter()

@router.post("/feedback")
def submit_feedback(feedback: Feedback):
    response = supabase.table("feedback").insert(feedback.dict()).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return response.data
