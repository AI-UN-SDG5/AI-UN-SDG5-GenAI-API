import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import datetime
import dotenv
dotenv.load_dotenv()
import google.generativeai as genai
import uuid

from DTO.Chat import Chat
from DTO.ChatMessage import ChatMessage
from DbConnection.DbConnection import DbConnection

class Chatbot:
    def __init__(self, chat_id):
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        self.id = None
        self.user_account = None
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.default_chat_intro = {"role": "model", "parts": "Hello. I am an intelligent chatbot here to help you wih your concerns about PCOS. What's on your mind?"}
        self.history = []
        self.created_at = datetime.datetime.now()
        self.db_connection = DbConnection()
        self.init_chat(chat_id)
    
    def init_chat(self, chat_id):
        try:
            chat_history = self.parse_chat_messages_from_db(chat_id)
            if len(chat_history) == 0:
                self.history.append(self.default_chat_intro)
                self.chat = self.model.start_chat(history=history)
                chat = Chat(str(self.id), str(self.user_account), self.created_at)
                chat_message = ChatMessage(str(uuid.uuid4()), str(self.id), str(self.user_account), "model", self.default_chat_intro["parts"], None, datetime.datetime.now())
                insert_chat_result = self.db_connection.insert_chat(chat)
                insert_chat_message_result = self.db_connection.insert_chat_message(chat_message)
                print(chat_message)
                print(f"Chat initialised: {insert_chat_result['id']}")
                print(f"Chat first message after initialisation: {insert_chat_message_result['id']}")
            else:
                print(f"Fetching data for existing chat: {chat_id}")
                self.history = chat_history

        except Exception as e:
            print(f"Exception initialising chat: {e}")
            raise Exception(f"Exception initialising chat: {e}") 

    def query_chatbot(self, message):
        try:
            user_chat_message = ChatMessage(
                str(uuid.uuid4()),
                str(self.id),
                self.user_account,
                "user",
                message,
                None,
                datetime.datetime.now()
            )
            response = self.chat.send_message(message)
            model_chat_message = ChatMessage(
                str(uuid.uuid4()),
                str(self.id),
                self.user_account,
                "model",
                response.text,
                None,
                datetime.datetime.now()
            )
            self.db_connection.insert_chat_message(user_chat_message)
            self.db_connection.insert_chat_message(model_chat_message)
            return response.text
        
        except Exception as e:
            print(f"Exception querying chat: {e}")
            return e

    def parse_chat_messages_from_db(self, chat_id):
        try:
            chat_messages: list[ChatMessage] = self.db_connection.fetch_chat_messages_by_chat_id(chat_id)
            history = []
            for message in chat_messages:
                history.append({"role": message.sender, "parts": message.message})
            return history
        except Exception as e:
            print(f"Exception parsing chat messages from db: {e}")
            return e

if __name__ == "__main__":

    # Test chatbot flow
    
    # Replace with a user_account id that already exists in database for testing the db_connection class
    placeholder_user_account_id = "51288e48-2fee-4881-be9e-7d021df734db"
    """chat = Chatbot(placeholder_user_account_id, [])
    print(chat.history[-1])
    end_chat = False
    user_query = input("Query chatbot: ")
    while not end_chat:
        response = chat.query_chatbot(user_query)
        print(response)
        user_query = input("Query chatbot: ")
        if user_query.strip().lower() == "q":
            end_chat = True"""
    
    
    placeholder_chat_id = "cffa1a06-8cc7-412c-9539-cdc26fdaf99c" # Replace with existing chat id for testing
    chat = Chatbot(placeholder_chat_id)
    chat_messages_by_chat_id = chat.parse_chat_messages_from_db(placeholder_chat_id)
    print("chat history after parsing: ", chat_messages_by_chat_id)
