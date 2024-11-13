class GeneratedMeal:
    def __init__(self, id, user_account, prompt, title, content, image_path, created_at):
        self.id = id
        self.user_account = user_account
        self.prompt = prompt
        self.title = title
        self.content = content
        self.image_path = image_path
        self.created_at = created_at

    def __str__(self):
        return f"{{\"id\": {self.id}, \"user_account\": {self.user_account}, \"prompt\": {self.prompt}, \"title\": {self.title}, \"content\": {self.content}, \"image_path\": {self.image_path}, \"created_at\": {self.created_at}}}"