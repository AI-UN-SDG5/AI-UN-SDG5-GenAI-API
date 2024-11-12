class Chat:
    def __init__(self, id, user_account, created_at):
        self.id = id
        self.user_account = user_account
        self.created_at = created_at

    def __str__(self):
        return f"{{\"id\": {self.id}, \"user_account\": {self.user_account}, \"created_at\": {self.created_at}}}"