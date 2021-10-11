'''
    Polished version of the homework

    This program accepts both int and float as the value types for calculating
    float can be given both with a dot and comma sign
'''
import calculator
import numbers_formatter

if __name__ == '__main__':
    while True:
        print('1: Oblicz średnią arytmetyczną')
        print('2: Podnieś do potęgi')
        print('3: Porównaj liczby')
        print('4: Zamknij progam')
        menu_decision = input('Wybierz jedną z opcji z menu: ')

        if menu_decision == "1":
            liczba_1 = numbers_formatter.number_input('Podaj pierwszą liczbę: ')
            liczba_2 = numbers_formatter.number_input('Podaj drugą liczbę: ')
            calculator.srednia_arytmetyczna(liczba_1, liczba_2)
        elif menu_decision == '2':
            liczba_1 = numbers_formatter.number_input('Podaj pierwszą liczbę: ')
            liczba_2 = numbers_formatter.number_input('Podaj drugą liczbę: ')
            calculator.potega(liczba_1, liczba_2)
        elif menu_decision == '3':
            liczba_1 = numbers_formatter.number_input('Podaj pierwszą liczbę: ')
            liczba_2 = numbers_formatter.number_input('Podaj drugą liczbę: ')
            calculator.porownywarka(liczba_1, liczba_2)
        elif menu_decision == '4':
            break
