class DietPreference:
    def __init__(self, id, user_account, diet):
        self.id = id
        self.user_account = user_account
        self.diet = diet

    def __str__(self):
        return f"{{\"id\": {self.id}, \"user_account\": {self.user_account}, \"diet\": {self.diet}}}"