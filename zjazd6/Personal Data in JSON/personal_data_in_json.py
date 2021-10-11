from phone_format_error import PhoneFormatError
from re import search


def personal_data_input():
    first_name = input('Podaj imię: ')
    last_name = input('Podaj nazwisko: ')
    try:
        telephone_no = input('Podaj numer telefonu: ')
        if phone_no_format_check(telephone_no):
            raise PhoneFormatError
    except PhoneFormatError as error:
        print(error.message)
    else:
        print('Lucky')


def phone_no_format_check(phone_no):
    allowed_formats = [r'[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]',
                       r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',
                       r'[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9]']
    match = search(r'[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]', phone_no)
    if not match:
        return True


if __name__ == '__main__':
    personal_data_input()
