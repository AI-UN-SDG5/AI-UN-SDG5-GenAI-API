import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

from ContentGenerator.ContentGenerator import ContentGenerator
from DTO.BloodType import BloodType
from DTO.CallingCode import CallingCode
from DTO.Chat import Chat
from DTO.ChatMessage import ChatMessage
from DTO.Country import Country
from DTO.Diet import Diet
from DTO.DietPreference import DietPreference
from DTO.GeneratedMeal import GeneratedMeal
from DTO.GeneratedWorkout import GeneratedWorkout
from DTO.MedicalAppointmentNote import MedicalAppointmentNote
from DTO.Sex import Sex
from DTO.SkinType import SkinType
from DTO.UserAccount import UserAccount

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the P for Pluma Generative AI API!"}

@app.post("/generate-medical-appointment-note")
async def root():
    return {"message": "Hello World. Welcome to the P for Pluma Generative AI API!"}