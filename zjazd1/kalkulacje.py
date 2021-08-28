while True:
    print('1: Oblicz średnią arytmetyczną')
    print('2: Podnieś do potęgi')
    print('3: Porównaj liczby')
    print('4: Zamknij progam')
    menu_decision = input('Wybierz jedną z opcji z menu: ')

    if menu_decision == "1":
        liczba_1 = int(input('Podaj pierwszą liczbę: '))
        liczba_2 = int(input('Podaj drugą liczbę: '))
        print(f'Średnia arytmetyczna wynosi: {(liczba_1 + liczba_2) / 2}\n')
    elif menu_decision == '2':
        liczba_1 = int(input('Podaj pierwszą liczbę: '))
        liczba_2 = int(input('Podaj drugą liczbę: '))
        print(f'Potęga wynosi {liczba_1 ** liczba_2}\n')
    elif menu_decision == '3':
        liczba_1 = int(input('Podaj pierwszą liczbę: '))
        liczba_2 = int(input('Podaj drugą liczbę: '))
        if liczba_1 != liczba_2:
            print(f'Liczba {max(liczba_1, liczba_2)} jest wyższa\n')
        else:
            print("Liczby są równe\n")
    elif menu_decision == '4':
        break
