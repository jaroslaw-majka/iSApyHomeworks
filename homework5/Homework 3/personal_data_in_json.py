from phone_format_error import PhoneFormatError
from re import search
import json
from sys import exit


def personal_data_input() -> dict:
    """Takes user input and returns a dict"""
    first_name = input('Podaj imię: ')
    last_name = input('Podaj nazwisko: ')
    try:
        telephone_no = input('Podaj numer telefonu: ')
        if not phone_no_format_valid(telephone_no):
            raise PhoneFormatError
    except PhoneFormatError as error:
        print(error.message)
        exit()
    else:
        print('Saving data now')
    return {'imię': first_name, 'nazwisko': last_name, 'telefon': telephone_no}


def phone_no_format_valid(phone_no) -> bool:
    """Checks given string (phone number) against patterns"""
    if len(phone_no) in [9, 11]:
        allowed_patterns = [r'[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]',
                            r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',
                            r'[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9]']
        for pattern in allowed_patterns:
            if search(pattern, phone_no):
                return True


def data_saving(data: dict):
    with open('phone_base.json', 'w') as write_file:
        json.dump(data, write_file)


if __name__ == '__main__':
    data_saving(personal_data_input())
