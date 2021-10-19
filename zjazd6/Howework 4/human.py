from datetime import datetime
from re import search


class Human:
    def __init__(self, first_name: str, last_name: str, date_of_birth: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
