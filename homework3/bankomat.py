accounts = {
    12345: {
        'pin': 1234,
        'saldo': 2345,
        'historia': []
    },
    23456: {
        'pin': 2222,
        'saldo': 5000
    }
}


def account_operations():
    acc_num = int(input('Podaj numer swojego konta: '))
    if acc_num in accounts:
        pin_code = int(input('Podaj numer PIN: '))
        if pin_code == accounts[acc_num]['pin']:
            account_options(acc_num)
        else:
            print('Podany PIN jest błędny')
    else:
        print('Podany numer konta nie istnieje.')


def user_decision():
    print('1. Sprawdź saldo')
    print('2. Wpłać pieniądze')
    print('3. Zmień kod PIN')
    print('4. Wyświetl historię')
    print('0. Zakończ')
    option = input('Wybierz jedną z opcji podająć numer do niej przypisany: ')
    return option


def account_options(acc_number: int):
    while True:
        decision = user_decision()
        if decision == '1':
            print(f"Saldo wynosi: {accounts[acc_number]['saldo']}")
            accounts[acc_number]['historia'].append(
                account_history('Sprawdzenie salda', accounts[acc_number]['saldo']))
        elif decision == '2':
            cash_in_ammount = int(input('Podaj kwotę, którą chcesz wpłacić: '))
            accounts[acc_number]['saldo'] += cash_in_ammount
            accounts[acc_number]['historia'].append(
                account_history('Wpłata', cash_in_ammount))
            print(f"Zaktualizowane saldo wynosi: {accounts[acc_number]['saldo']}")
        elif decision == '3':
            new_pin = int(input('Podaj nowy kod PIN: '))
            accounts[acc_number]['pin'] = new_pin
            print(accounts[acc_number]['pin'])
            accounts[acc_number]['historia'].append(
                account_history('Zmiana numeru PIN', new_pin))
        elif decision == '4':
            history_list = accounts[acc_number]['historia']
            print(history_list)
            for i in range(len(history_list)):
                print(f"Operacja: {history_list[i][0]}, zmiana: {history_list[i][1]}")
        elif decision == '0':
            break


def account_history(user_decision, operation):
    return (user_decision, operation)


if __name__ == '__main__':
    account_operations()
