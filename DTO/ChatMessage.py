class ChatMessage:
    def __init__(self, id, user_account, sender, message, image_path, created_at):
        self.id = id
        self.user_account = user_account
        self.sender = sender
        self.message = message
        self.image_path = image_path
        self.created_at = created_at

    def __str__(self):
        return f"{{\"id\": {self.id}, \"user_account\": {self.user_account}, \"sender\": {self.sender}, \"message\": {self.message}, \"image_path\": {self.image_path}, \"created_at\": {self.created_at}}}"