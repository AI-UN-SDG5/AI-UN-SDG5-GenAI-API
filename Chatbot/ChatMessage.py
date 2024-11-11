from datetime import datetime, timezone
from uuid import uuid4

class ChatMessage:
    
    def __init__(self, sender, message, init_timestamp=None, index=0):
        self.id = uuid4()
        self.sender = sender
        self.message = message
        if init_timestamp == None:
            self.init_timestamp = self.get_current_utc_timestamp_string()
        else: 
            self.init_timestamp = init_timestamp
        self.index = index
    
    def get_current_utc_timestamp_string(self):
        now = datetime.now(timezone.utc)
        return now.strftime("%Y-%m-%dT%XZ")
    
    def __str__(self):
        return f"Chat Message\n-----------------------\nid: {self.id}\nindex: {self.index}\nsender: {self.sender}\nmessage: {self.message}\ninit_timestamp: {self.init_timestamp}"