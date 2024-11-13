class SkinType:
    def __init__(self, id, skin_type, description):
        self.id = id
        self.skin_type = skin_type
        self.description = description
    
    def __str__(self):
        return f"{{ \"id\": {self.id},  \"skin_type\": {self.skin_type}, \"description\": {self.description}}}"