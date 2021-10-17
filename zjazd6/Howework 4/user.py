import datetime

from human import Human


class User(Human):
    def __init__(self, first_name: str, last_name: str, date_of_birth: str):
        super().__init__(first_name, last_name, date_of_birth)
        self._age = None

    @property
    def age(self) -> int:
        if self._age:
            return self._age
        year_of_birth = int(self.date_of_birth.split('/')[2])
        current_year = datetime.datetime.now().year
        return current_year - year_of_birth
