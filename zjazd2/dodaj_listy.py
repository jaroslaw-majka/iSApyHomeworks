# Stwórz funkcję nazwaną dodajListy() która zwróci nową listę sumując ze sobą elementy na tych samych indeksach.
# Możesz przypuścić, że jako parametry do funkcji podawane są zawsze listy zawierające tylko liczby.
# Jeżeli listy są różnej długości, funkcja powinna wyświetlić napis ‘Podane listy muszą być tej samej długości’

def dodaj_listy(list_1, list_2):
    summed_list = []
    if len(list_1) != len(list_2):
        return 'Podane listy muszą być tej samej długości.'
    else:
        for idx in range(len(list_1)):
            summed_list.insert(idx, list_1[idx] + list_2[idx])
    return summed_list
