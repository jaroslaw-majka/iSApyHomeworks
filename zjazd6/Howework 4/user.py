from human import Human


class User(Human):
    def __init__(self, first_name: str, last_name: str, date_of_birth: str):
        super().__init__(first_name, last_name, date_of_birth)

    def get_age(self):
        return self._age


if __name__ == '__main__':
    uzytkownik = User('Jarek', 'Majka', '01/01/2000')
    print(uzytkownik.first_name)
    print(uzytkownik.last_name)
    print(uzytkownik.date_of_birth)
    print(uzytkownik.get_age())
