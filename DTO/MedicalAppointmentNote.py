class MedicalAppointmentNote:
    def __init__(self, id, user_account, title, content, insights, created_at, generated_insights_at, updated_at, generated_insights_updated_at):
        self.id = id
        self.user_account = user_account
        self.title = title
        self.content = content
        self.insights = insights
        self.created_at = created_at
        self.generated_insights_at = generated_insights_at
        self.updated_at = updated_at
        self.generated_insights_updated_at = generated_insights_updated_at

    def __str__(self):
        return f"{{\"id\":{self.id}, \"user_account\":{self.user_account}, \"title\":{self.title}, \"content\":{self.content}, \"insights\":{self.insights}, \"created_at\":{self.generated_insights_at}, \"updated_at\":{self.updated_at}, \"generated_insights_updated_at\":{self.generated_insights_at}}}"