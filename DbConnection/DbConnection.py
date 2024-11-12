import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from DTO.UserAccount import UserAccount
from DTO.SkinType import SkinType
from DTO.Sex import Sex
from DTO.MedicalAppointmentNote import MedicalAppointmentNote
from DTO.GeneratedWorkout import GeneratedWorkout
from DTO.GeneratedMeal import GeneratedMeal
from DTO.DietPreference import DietPreference
from DTO.Diet import Diet
from DTO.Country import Country
from DTO.ChatMessage import ChatMessage
from DTO.Chat import Chat
from DTO.CallingCode import CallingCode
from DTO.BloodType import BloodType
import uuid
import psycopg2
import os
import datetime
from django.db import connection
import dotenv
dotenv.load_dotenv()


class DbConnection:
    def __init__(self):
        self.DB_URL = f"postgres://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{
            os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"
    
    def insert_medical_appointment_note(self, medical_appointment_note: MedicalAppointmentNote):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()
            
            query = "INSERT INTO medical_appointment_note (id, user_account, title, content, insights, created_at, generated_insights_at, updated_at, generated_insights_updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (medical_appointment_note.id, medical_appointment_note.user_account, medical_appointment_note.title, medical_appointment_note.content, medical_appointment_note.insights,medical_appointment_note.created_at, medical_appointment_note.generated_insights_at, medical_appointment_note.updated_at, medical_appointment_note.generated_insights_updated_at)
            result = cursor.execute(query, data)
            cursor.close()
            return {
                "id": medical_appointment_note.id
            }

        except Exception as e:
            print(f"Error inserting medical appointment note insights: {e}")
            return e

    def insert_generated_workout(self, generated_workout: GeneratedWorkout):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()
            
            query = "INSERT INTO generated_workout (id, user_account, prompt, title, content, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (generated_workout.id, generated_workout.user_account, generated_workout.prompt, generated_workout.title, generated_workout.content, generated_workout.created_at)
            result = cursor.execute(query, data)
            cursor.close()
            return {
                "id": generated_workout.id
            }

        except Exception as e:
            print(f"Error inserting generated workout: {e}")
            return e
        
    def insert_generated_meal(self, generated_meal: GeneratedMeal):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()
            
            query = "INSERT INTO generated_meal (id, user_account, prompt, title, content, image_path, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (generated_meal.id, generated_meal.user_account, generated_meal.prompt, generated_meal.title, generated_meal.content, generated_meal.image_path, generated_meal.created_at)
            result = cursor.execute(query, data)
            cursor.close()
            return {
                "id": generated_meal.id
            }

        except Exception as e:
            print(f"Error inserting generated meal: {e}")
            return e
        
if __name__ == "__main__":

    dbConnection: DbConnection = DbConnection()
    placeholder_user_account_id = "51288e48-2fee-4881-be9e-7d021df734db" # replace with a user_account id that already exists in database for testing the DbConnection class
    
    # Run script to see if a placeholder medical appointment note is correctly inserted into the database
    medical_appointment_note = MedicalAppointmentNote(
        str(uuid.uuid4()),
        placeholder_user_account_id,
        "Medical Appointment Note Title",
        "Feel sick",
        None,
        datetime.datetime.now(),
        None,
        None,
        None
    )
    results = dbConnection.insert_medical_appointment_note(medical_appointment_note)
    print("medical_appointment_note: ", results)
    
    # Run script to see if a placeholder generated workout is correctly inserted into the database
    generated_workout = GeneratedWorkout(
        str(uuid.uuid4()),
        placeholder_user_account_id,
        "I want toned thighs",
        "Power up today!",
        "30 min run, 100 jumping jacks, 200 squats",
        datetime.datetime.now(),
    )
    results = dbConnection.insert_generated_workout(generated_workout)
    print("generated_workout: ", results)

    # Run class to see if a placeholder generated meal is correctly inserted into the database
    generated_meal = GeneratedMeal(
        str(uuid.uuid4()),
        placeholder_user_account_id,
        "Something sweet with strawberries",
        "Strawberry Smoothie",
        "Healthy and sweet strawberry smoothie - 1/2 cup milk, 1 cup strawberries, 2 tbsp honey",
        f"/tmp/{uuid.uuid4()}.png",
        datetime.datetime.now(),
    )
    results = dbConnection.insert_generated_meal(generated_meal)
    print("generated_meal: ", results)