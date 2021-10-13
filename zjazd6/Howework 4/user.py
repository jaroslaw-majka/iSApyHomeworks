import datetime

from human import Human


class User(Human):
    def __init__(self, first_name: str, last_name: str, date_of_birth: str):
        super().__init__(first_name, last_name, date_of_birth)
        self.set_age(date_of_birth)

    def get_age(self) -> int:
        """Protected variable _age getter"""
        return self._age

    def set_age(self, date_of_birth) -> None:
        """Age setter based on provided date of birth"""
        year_of_birth = int(date_of_birth.split('/')[2])
        current_year = datetime.datetime.now().year
        self._age = current_year - year_of_birth
