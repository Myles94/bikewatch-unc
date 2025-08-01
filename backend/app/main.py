from fastapi import FastAPI
from .routes import report, sightings, feedback


app = FastAPI()

@app.get("/")

def root():
    return {"message": "BikeWatch API Running"}

app.include_router(report.router)
app.include_router(sightings.router)
app.include_router(feedback.router)