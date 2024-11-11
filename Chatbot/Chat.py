from datetime import datetime, timezone
import sys
sys.path.append('.Chatbot') 
from Chatbot.ChatMessage import ChatMessage
from uuid import uuid4

class Chat:
    def __init__(self):
        self.id = uuid4()
        self.init_timestamp = self.get_current_utc_timestamp_string()
        self.messages= []
        self.add_message("chatbot", "Hello. I am an intelligent chatbot here to help you wih your concerns about PCOS. What's on your mind?")

    def add_message_old(self, message):
        self.messages.append(message)
    
    def add_message(self, sender, message, timestamp=None, index=0):
        self.messages.append(ChatMessage(sender, message, timestamp, len(self.messages)))
    
    def get_messages(self):
        return self.messages
    
    def get_messages_as_string(self):
        final_messages_string = "["
        for index, message in enumerate(self.messages):
            final_messages_string += f'{{"id": "{message.id}", "index": {message.index}, "sender": "{message.sender}", "message": "{message.message}", "init_timestamp": "{message.init_timestamp}"}}'
            if index < len(self.messages) - 1:
                final_messages_string += ", "
        final_messages_string += "]"
        return final_messages_string

    def get_current_utc_timestamp_string(self):
        now = datetime.now(timezone.utc)
        return now.strftime("%Y-%m-%dT%XZ")
    
    def __str__(self):
        return f"Chatbot\n----------\nid: {self.id}\ninit_time: {self.init_timestamp}\nmessage_count: {len(self.messages)}"