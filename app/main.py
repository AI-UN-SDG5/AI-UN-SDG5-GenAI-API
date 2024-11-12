from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import uuid

from ..ContentGenerator.ContentGenerator import ContentGenerator
from ..ContentGenerator.GeneratedMeal import GeneratedMeal
from ..ContentGenerator.GeneratedWorkout import GeneratedWorkout
from ..ContentGenerator.MedicalAppointmentNoteInsight import MedicalAppointmentNoteInsight

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the P for Pluma Generative AI API!"}