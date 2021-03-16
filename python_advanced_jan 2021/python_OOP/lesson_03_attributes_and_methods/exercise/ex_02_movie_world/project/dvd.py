class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}." \
               f" Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        date_mapper = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "June",
            "06": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }
        data = date.split(".")
        creation_month = str(date_mapper[data[1]])
        creation_year = int(data[2])

        return cls(id=id, name=name, creation_year=creation_year, creation_month=creation_month, age_restriction=age_restriction)
