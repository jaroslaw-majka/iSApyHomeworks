# Stwórz funkcję nazwaną zbadajTrojkat() która przyjmie jako argumenty długości boków trójkąta.
# Funkcja powinna zwrócić, czy trójkąt jest prostokątny, równoramienny, równoboczny, różnoboczny lub nieprawidłowy
def zbadaj_trojkat(side_a, side_b, side_c):
    if side_a + side_b > side_c \
            and side_a + side_c > side_b \
            and side_b + side_c > side_a:
        # prostokątny
        if side_a ** 2 + side_b ** 2 == side_c ** 2 \
                or side_a ** 2 + side_c ** 2 == side_b ** 2 \
                or side_b ** 2 + side_c ** 2 == side_a ** 2:
            return 'Trójkąt prostokątny'
        # równoramienny
        elif side_a == side_b == side_c:
            return 'Trójkąt równoramienny'
        # równoboczny
        elif side_a == side_b \
                or side_a == side_c \
                or side_b == side_c:
            return 'Trójkąt równoboczny'
        # różnoboczny
        else:
            return 'Trójkąt różnoboczny'
    else:
        return 'Trójkąt nieprawidłowy'
