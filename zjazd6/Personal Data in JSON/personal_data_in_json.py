from phone_format_error import PhoneFormatError
from re import search


def personal_data_input():
    first_name = input('Podaj imię: ')
    last_name = input('Podaj nazwisko: ')
    try:
        telephone_no = input('Podaj numer telefonu: ')
        if not phone_no_format_check(telephone_no):
            raise PhoneFormatError
    except PhoneFormatError as error:
        print(error.message)
    return {(first_name, last_name): telephone_no}


def phone_no_format_check(phone_no):
    allowed_patterns = [r'[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]',
                        r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',
                        r'[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9]']
    match = []
    for pattern in allowed_patterns:
        if search(pattern, phone_no):
            match.append(True)
        else:
            match.append(False)
    if len(phone_no) != 9 or len(phone_no) != 11:
        return False
    if True in match:
        return True


if __name__ == '__main__':
    personal_data_input()
