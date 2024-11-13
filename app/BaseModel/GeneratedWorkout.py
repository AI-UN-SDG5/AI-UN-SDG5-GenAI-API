import datetime
from pydantic import BaseModel
import uuid

class GeneratedWorkout(BaseModel):
    id: str = str(uuid.uuid4())
    user_account: str = ""
    prompt: str = ""
    title: str = "Generated Workout Title"
    content: str = "Generated Workout Content"
    created_at: datetime.datetime = datetime.datetime.now()