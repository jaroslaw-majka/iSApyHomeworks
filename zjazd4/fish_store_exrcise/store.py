from dry_stock import DryStock
from livestock import FishStock


class Store:
    livestock_list = []
    drystock_list = []

    def __init__(self):
        self.main()

    def menu_interface(self):
        print('1. Dodaj ryby na stan')
        print('2. Dodaj suche produkty na stan')
        print('3. Wyświetl dostępne ryby')
        print('4. Wyświetl dostępne suche produkty')
        print('5. Sprzedaj rybę')
        print('6. Sprzedaj suchy produkt')
        # print('7. Dodaj nową kartę klienta')
        # print('8. Wyświetl punkty klienta')
        print('0. Zamknij program')
        return input('Wybierz jedną z opcji: ')

    def livestock_name_check(self, name=''):
        if not name:
            name = input('Jakiej ryby szukasz: ')
        for fish in Store.livestock_list:
            if fish.name == name:
                return fish

    def adding_livestock(self):
        fish_name = input('Podaj nazwę ryby: ')
        amount = int(input('Ile sztuk dodajesz: '))
        fish_present = self.livestock_name_check(fish_name)
        if fish_present:
            fish_present.amount += amount
        else:
            freshwater = bool(input('Czy ryba jest słodkowodna? y/N'))
            fish_origin = input('Skąd ryba pochodzi: ')
            Store.livestock_list.append(FishStock(fish_name, fish_origin, amount, freshwater))

    def livestock_display(self):
        [print(f'Nazwa: {fish.name}\n'
               f'Pochodzenie: {fish.origin}\n'
               f'Ilość sztuk: {fish.amount}\n') for fish in Store.livestock_list]

    def livestock_sale(self):
        def livestock_amount_check(fish_obj, amount_for_sale):
            return fish_obj.amount >= amount_for_sale

        fish_for_sale = self.livestock_name_check()
        if fish_for_sale:
            amount = int(input(f'Ile {fish_for_sale.name} chciałbyś sprzedać: '))
            if livestock_amount_check(fish_for_sale, amount):
                fish_for_sale.make_a_sale(amount)
            else:
                print('Nie masz wystarczającej liczby ryb.')
        else:
            print('Nie masz takie ryby na stanie.')

    def adding_dry_stock(self):
        item_name = input('Podaj nazwę produktu: ')
        item_type = input('Podaj rodzaj (karma, akwarium, akcesoria) produktu: ')
        item_brand = input('Podaj markę produktu: ')
        amount = int(input('Ile sztuk dodajesz: '))
        # TODO Sprawdź, czy ten przedmiot istnieje i jeżel itak to dodaj do stanu
        Store.drystock_list.append(DryStock(item_name, item_type, item_brand, amount))

    def drystock_display(self):
        for item in Store.drystock_list:
            item.print_dry_stock_list()

    def dry_stock_sale(self):
        def dry_stock_name_check():
            name = input('Jaki przedmiot sprzedajesz: ')
            for item in Store.drystock_list:
                if item.item_name == name:
                    return item

        def dry_stock_amount_check(item_obj, amount):
            return item_obj.stock >= amount

        item_for_sale = dry_stock_name_check()
        if item_for_sale:
            amount = int(input('Ile sztuk sprzedajesz: '))
            if dry_stock_amount_check(item_for_sale, amount):
                item_for_sale.make_a_sale(amount)
        else:
            print('Nie ma tego produktu na stanie.')

    def main(self):
        while True:
            menu_choice = self.menu_interface()
            if menu_choice == '0':
                break
            elif menu_choice == '1':
                self.adding_livestock()
            elif menu_choice == '2':
                self.adding_dry_stock()
            elif menu_choice == '3':
                self.livestock_display()
            elif menu_choice == '4':
                self.drystock_display()
            elif menu_choice == '5':
                self.livestock_sale()
            elif menu_choice == '6':
                self.dry_stock_sale()


if __name__ == '__main__':
    Store()
