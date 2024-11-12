class UserAccount:
    def __init__(self, id, email, is_google_authenticated, password, first_name, last_name, 
                        birthdate, sex, address, country, calling_code, phone_number, created_at, 
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
        self.created_at = created_at
        self.verified_at = verified_at
        self.last_login_at = last_login_at
        self.password_updated_at = password_updated_at
        self.personal_details_updated_at = personal_details_updated_at
        self.account_status = account_status
        self.account_status_updated_at = account_status_updated_at
