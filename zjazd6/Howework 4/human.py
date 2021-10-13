from re import search


class Human:
    def __init__(self, first_name: str, last_name: str, date_of_birth: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = self.birth_date_validator(date_of_birth)
        self._age = 1

    def birth_date_validator(self, date_of_birth):
        date_format_pattern = r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]'
        if search(date_format_pattern, date_of_birth):
            return date_of_birth
        else:
            raise Exception('Invalid date format. Please use dd/mm/yyyy')
