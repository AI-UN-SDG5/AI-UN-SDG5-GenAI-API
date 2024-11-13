class Diet:
    def __init__(self, id, diet, description):
        self.id = id
        self.diet = diet
        self.description = description

    def __str__(self):
        return f"{{ \"id\": {self.id},  \"diet\": {self.diet}, \"description\": {self.description}}}"