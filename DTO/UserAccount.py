class UserAccount:
    def __init__(self, id, email, is_google_authenticated, password, first_name, last_name,
                 birthdate, sex, address, country, calling_code, phone_number, height, mass, blood_type, skin_type, created_at,
                 verified_at, last_login_at, password_updated_at, personal_details_updated_at,
                 account_status, account_status_updated_at):
        self.id = id
        self.email = email
        self.is_google_authenticated = is_google_authenticated
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.sex = sex
        self.address = address
        self.country = country
        self.calling_code = calling_code
        self.phone_number = phone_number
        self.height = height
        self.mass = mass
        self.blood_type = blood_type
        self.skin_type = skin_type
        self.created_at = created_at
        self.verified_at = verified_at
        self.last_login_at = last_login_at
        self.password_updated_at = password_updated_at
        self.personal_details_updated_at = personal_details_updated_at
        self.account_status = account_status
        self.account_status_updated_at = account_status_updated_at

    def __str__(self):
        return f"{{\"id\": {self.id}, \"email\": {self.email}, \"is_google_authenticated\": {self.is_google_authenticated}, \"password\": {self.password}, \"first_name\": {self.first_name}, \"last_name\": {self.last_name}, \"birthdate\": {self.birthdate}, \"sex\": {self.sex}, \"address\": {self.address}, \"country\": {self.country}, \"calling_code\": {self.calling_code}, \"phone_number\": {self.phone_number}, \"height\": {self.height}, \"mass\": {self.mass}, \"blood_type\": {self.blood_type}, \"skin_type\": {self.skin_type}, \"created_at\": {self.created_at}, \"verified_at\": {self.verified_at}, \"last_login_at\": {self.last_login_at}, \"password_updated_at\": {self.password_updated_at}, \"personal_details_updated_at\": {self.personal_details_updated_at}, \"account_status\": {self.account_status}, \"account_status_updated_at\": {self.account_status_updated_at}}}"
