class BloodType:
    def __init__(self, id, blood_type, description):
        self.id = id
        self.blood_type = blood_type
        self.description = description

    def __str__(self):
        return f"{{ \"id\": {self.id},  \"blood_type\": {self.blood_type}, \"description\": {self.description}}}"