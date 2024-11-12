import datetime
from pydantic import BaseModel
import uuid

class MedicalAppointmentNoteInsight(BaseModel):
    id: str = str(uuid.uuid4())
    user_account: str
    title: str = "Medical Appointment Note Title"
    content: str | None = ""
    insights: str = ""
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime | None = None
    generated_insights_updated_at: datetime.datetime | None = None