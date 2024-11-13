import datetime
from pydantic import BaseModel
import uuid

class GeneratedMeal(BaseModel):
    id: str = str(uuid.uuid4())
    user_account: str = ""
    prompt: str = ""
    title: str = "Generated Meal Title"
    content: str = "Generated Meal Content"
    image_path: str | None = None
    created_at: datetime.datetime = datetime.datetime.now()