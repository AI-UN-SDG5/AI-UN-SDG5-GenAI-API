class CallingCode:
    def __init__(self, id, country, calling_code):
        self.id = id
        self.country = country
        self.calling_code = calling_code

    def __str__(self):
        return f"{{\"id\": {self.id}, \"country\": {self.country}, \"calling_code\": {self.calling_code}}}"