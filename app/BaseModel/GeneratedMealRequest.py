import datetime
from pydantic import BaseModel
import uuid

class GeneratedMealRequest(BaseModel):
    user_account: str = ""
    prompt: str = ""
    created_at: datetime.datetime = datetime.datetime.now()