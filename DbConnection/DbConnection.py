import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import dotenv
dotenv.load_dotenv()
from django.db import connection
import datetime
import psycopg2
import uuid
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

class DbConnection:
    def __init__(self):
        self.DB_URL = f"postgres://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{
            os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"

    def fetch_user_account_by_id(self, user_id: str):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "SELECT * from user_account WHERE id = %s"
            data = (user_id, )
            cursor.execute(query, data)
            result = cursor.fetchone()
            cursor.close()
            user_account = UserAccount(
                result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[
                    9], result[10], result[11], result[12], result[13], result[14], result[15], result[16], result[17], result[18],
                    result[19], result[20], result[21], result[22]
            )
            return user_account

        except Exception as e:
            print(f"Error fetching user account by id {user_id}: {e}")
            return e
        
    def fetch_sex_by_id(self, sex_id: str):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "SELECT * from sex WHERE id = %s"
            data = (sex_id, )
            cursor.execute(query, data)
            result = cursor.fetchone()
            cursor.close()
            sex = Sex(result[0], result[1], result[2], result[3])
            return sex

        except Exception as e:
            print(f"Error fetching sex by id {sex_id}: {e}")
            return e
        
    def fetch_blood_type_by_id(self, blood_type_id: str):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "SELECT * from blood_type WHERE id = %s"
            data = (blood_type_id, )
            cursor.execute(query, data)
            result = cursor.fetchone()
            cursor.close()
            blood_type = BloodType(result[0], result[1], result[2])
            return blood_type

        except Exception as e:
            print(f"Error fetching blood type by id {blood_type_id}: {e}")
            return e
    
    def fetch_skin_type_by_id(self, skin_type_id: str):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "SELECT * from skin_type WHERE id = %s"
            data = (skin_type_id, )
            cursor.execute(query, data)
            result = cursor.fetchone()
            cursor.close()
            skin_type = SkinType(result[0], result[1], result[2])
            return skin_type

        except Exception as e:
            print(f"Error fetching skin type by id {skin_type_id}: {e}")
            return e
        
    def fetch_diet_by_id(self, diet_id: str):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "SELECT * from diet WHERE id = %s"
            data = (diet_id, )
            cursor.execute(query, data)
            result = cursor.fetchone()
            cursor.close()
            diet = Diet(result[0], result[1], result[2])
            return diet

        except Exception as e:
            print(f"Error fetching diet by id {diet_id}: {e}")
            return e

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
            data = (medical_appointment_note.id, medical_appointment_note.user_account, medical_appointment_note.title, medical_appointment_note.content, medical_appointment_note.insights,
                    medical_appointment_note.created_at, medical_appointment_note.generated_insights_at, medical_appointment_note.updated_at, medical_appointment_note.generated_insights_updated_at)
            result = cursor.execute(query, data)
            cursor.close()
            return {
                "id": medical_appointment_note.id
            }

        except Exception as e:
            print(f"Error inserting medical appointment note: {e}")
            return e

    def insert_medical_appointment_note_insights(self, medical_appointment_note: MedicalAppointmentNote):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "UPDATE medical_appointment_note SET insights = %s, generated_insights_at = %s WHERE id = %s"
            data = (medical_appointment_note.insights,
                    medical_appointment_note.generated_insights_at, medical_appointment_note.id)
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
            data = (generated_workout.id, generated_workout.user_account, generated_workout.prompt,
                    generated_workout.title, generated_workout.content, generated_workout.created_at)
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
            data = (generated_meal.id, generated_meal.user_account, generated_meal.prompt, generated_meal.title,
                    generated_meal.content, generated_meal.image_path, generated_meal.created_at)
            result = cursor.execute(query, data)
            cursor.close()
            return {
                "id": generated_meal.id
            }

        except Exception as e:
            print(f"Error inserting generated meal: {e}")
            return e
        
    def insert_chat(self, chat: Chat):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "INSERT INTO chat (id, user_account, created_at) VALUES (%s, %s, %s)"
            data = (chat.id, chat.user_account, datetime.datetime.now())
            result = cursor.execute(query, data)
            cursor.close()
            return {
                "id": chat.id
            }

        except Exception as e:
            print(f"Error inserting chat: {e}")
            return e
        
    def insert_chat_message(self, chat_message: ChatMessage):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "INSERT INTO chat_message (id, chat, user_account, sender, message, image_path, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (chat_message.id, chat_message.chat, chat_message.user_account, chat_message.sender, chat_message.message, chat_message.image_path, datetime.datetime.now())
            result = cursor.execute(query, data)
            cursor.close()
            return {
                "id": chat_message.id
            }

        except Exception as e:
            print(f"Error inserting chat message: {e}")
            return e
        
    def fetch_chat_messages_by_chat_id(self, chat_id: str):
        try:
            connection = psycopg2.connect(
                host=os.environ.get('DB_HOST'),
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
            )
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            query = "SELECT * FROM chat_message WHERE chat = %s ORDER BY created_at ASC"
            data = (chat_id, )
            cursor.execute(query, data)
            result = cursor.fetchall()
            chat_messages = []
            for entry in result:
                chat_messages.append(ChatMessage(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]))
            cursor.close()
            return chat_messages

        except Exception as e:
            print(f"Error fetching chat messages by chat id: {e}")
            return e

    """def parse_chat_history(self, chat_id):
        db_connection = DbConnection()
        chat_messages_for_chat_id = db_connection.fetch_chat_messages_by_chat_id(chat_id)"""

if __name__ == "__main__":

    db_connection: DbConnection = DbConnection()
    # replace with a user_account id that already exists in database for testing the db_connection class
    placeholder_user_account_id = "51288e48-2fee-4881-be9e-7d021df734db"

    """user_account: UserAccount = db_connection.fetch_user_account_by_id(
        placeholder_user_account_id)
    print(user_account)

    sex: Sex = db_connection.fetch_sex_by_id(
        user_account.sex)
    print(sex)

    blood_type: BloodType = db_connection.fetch_blood_type_by_id(
        user_account.blood_type)
    print(blood_type)

    skin_type: BloodType = db_connection.fetch_skin_type_by_id(
        user_account.skin_type)
    print(skin_type)"""

    # diet_preferences= []

    # Run script to see if a placeholder medical appointment note is correctly inserted into the database
    """medical_appointment_note = MedicalAppointmentNote(
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
    results = db_connection.insert_medical_appointment_note(medical_appointment_note)
    print("medical_appointment_note: ", results)"""

    # Run script to see if a placeholder medical appointment note insights are correctly inserted
    """placeholder_medical_appointment_note_id = "92b13c3f-7b90-49e7-bca4-c0a2bf47119c"
    medical_appointment_note_insights = MedicalAppointmentNote(
        placeholder_medical_appointment_note_id,
        placeholder_user_account_id,
        "Medical Appointment Note Title",
        "Feel sick",
        "Generated insights placeholder",
        datetime.datetime.now(),
        datetime.datetime.now(),
        None,
        None
    )
    results = db_connection.insert_medical_appointment_note_insights(medical_appointment_note_insights)
    print("medical_appointment_note_insights: ", results)"""

    # Run script to see if a placeholder generated workout is correctly inserted into the database
    """generated_workout = GeneratedWorkout(
        str(uuid.uuid4()),
        placeholder_user_account_id,
        "I want toned thighs",
        "Power up today!",
        "30 min run, 100 jumping jacks, 200 squats",
        datetime.datetime.now(),
    )
    results = db_connection.insert_generated_workout(generated_workout)
    print("generated_workout: ", results)"""

    # Run class to see if a placeholder generated meal is correctly inserted into the database
    """generated_meal = GeneratedMeal(
        str(uuid.uuid4()),
        placeholder_user_account_id,
        "Something sweet with strawberries",
        "Strawberry Smoothie",
        "Healthy and sweet strawberry smoothie - 1/2 cup milk, 1 cup strawberries, 2 tbsp honey",
        f"/tmp/{uuid.uuid4()}.png",
        datetime.datetime.now(),
    )
    results = db_connection.insert_generated_meal(generated_meal)
    print("generated_meal: ", results)"""

    """chat = Chat(str(uuid.uuid4()), placeholder_user_account_id, datetime.datetime.now())
    result = db_connection.insert_chat(chat)
    print(result)

    chat_message = ChatMessage(
        str(uuid.uuid4()), 
        chat.id,
        placeholder_user_account_id, 
        "sender",
        "What can I do about my irregular period cycle?",
        None,
        datetime.datetime.now()
    )
    result = db_connection.insert_chat_message(chat_message)
    print(result)"""

    placeholder_chat_id = "cffa1a06-8cc7-412c-9536-cdc26fdaf99c" # Replace with existing chat id for testing
    result = db_connection.fetch_chat_messages_by_chat_id(placeholder_chat_id)
    for entry in result:
        print(entry)
        print("\n\n\n\n\n\n\n")