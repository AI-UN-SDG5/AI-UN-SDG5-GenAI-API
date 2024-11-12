class Sex:
    def __init__(self, id, code, sex, icon_path):
        self.id = id
        self.code = code
        self.sex = sex
        self.icon_path = icon_path

    def __str__(self):
        return f"{{ \"id\": {self.id},  \"code\": {self.code}, \"sex\": {self.sex}, \"icon_path\": {self.icon_path}}}"