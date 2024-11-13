class Country:
    def __init__(self, id, country, iso2, iso3, flag_icon_path):
        self.id = id
        self.country = country
        self.iso2 = iso2
        self.iso3 = iso3
        self.flag_icon_path = flag_icon_path
    
    def __str__(self):
        return f"{{\"id\": {self.id}, \"country\": {self.country}, \"iso2\": {self.iso2}, \"iso3\": {self.iso3}, \"flag_icon_path\": {self.flag_icon_path}}}"