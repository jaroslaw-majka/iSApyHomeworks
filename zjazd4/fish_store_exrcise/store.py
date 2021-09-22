from dry_stock import DryStock
from livestock import FishStock
from customers import LoyaltyCard
from data_management import DataManager


class Store:
    livestock_list = []
    dry_stock_list = []
    card_list = []

    def __init__(self):
        self.main()

    def menu_interface(self) -> str:
        '''
        Prints out menu
        :return: menu
        '''
        print('1. Dodaj ryby na stan')
        print('2. Dodaj suche produkty na stan')
        print('3. Wyświetl dostępne ryby')
        print('4. Wyświetl dostępne suche produkty')
        print('5. Sprzedaj rybę')
        print('6. Sprzedaj suchy produkt')
        print('7. Dodaj nową kartę klienta')
        print('8. Wyświetl punkty klienta i historię zakupów')
        print('0. Zamknij program')
        return input('Wybierz jedną z opcji: ')

    def livestock_name_check(self, name='') -> object:
        '''
        Checks if object already is present in livestock_list
        If true returns an object
        :param name: name of the searched object
        :return: object
        '''
        if not name:
            name = input('Jakiej ryby szukasz: ')
        for fish in Store.livestock_list:
            if fish.name == name:
                return fish

    def adding_livestock(self) -> None:
        '''
        Creates an instance of FishStock class and stores it in livestock_list
        If such instance already exists updates stock quantity
        :return: instance of FishStock class or updated stock
        '''
        fish_name = input('Podaj nazwę ryby: ')
        try:
            amount = int(input('Ile sztuk dodajesz: '))
        except ValueError:
            return print('To nie jest liczba całkowita.')
        fish_present = self.livestock_name_check(fish_name)
        if fish_present:
            fish_present.amount += amount
        else:
            freshwater = bool(input('Czy ryba jest słodkowodna? y/N'))
            fish_origin = input('Skąd ryba pochodzi: ')
            Store.livestock_list.append(FishStock(fish_name, fish_origin, amount, freshwater))

    def livestock_display(self) -> None:
        '''
        Prints live stock using list comprehension.
        :return: Fish stock
        '''
        [print(f'Nazwa: {fish.name}, '
               f'Pochodzenie: {fish.origin}, '
               f'Ilość sztuk: {fish.amount}') for fish in Store.livestock_list]

    def livestock_sale(self) -> None:
        '''
        Checks for desired fish in stock:
            If not available prints out information.
            If available takes user input of how many fish he would like to buy.
                If not available prints out information
                If available deducts quantity from stock, adds information on loyalty card if possible.
        :return: updated stock and loyalty card operations
        '''
        fish_for_sale = self.livestock_name_check()
        if fish_for_sale:
            try:
                amount = int(input(f'Ile {fish_for_sale.name} chciałbyś sprzedać: '))
            except ValueError:
                return print('To nie jest liczba całkowita.')
            if fish_for_sale.amount >= amount:
                fish_for_sale.make_a_sale(amount)
                self.loyalty_points_incrementator(amount, fish_for_sale.name)
            else:
                print('Nie masz wystarczającej liczby ryb.')
        else:
            print('Nie masz takie ryby na stanie.')

    def dry_stock_name_check(self, name='') -> object:
        '''
        Checks if object already is present in dry_stock_list
        If true returns an object
        :param name: name of the searched object
        :return: object
        '''
        if not name:
            name = input('Jaki przedmiot sprzedajesz: ')
        for item in Store.dry_stock_list:
            if item.name == name:
                return item

    def adding_dry_stock(self) -> None:
        '''
        Creates an instance of DryStock class and stores it in dry_stock_list
        If such instance already exists updates stock quantity
        :return: instance of DryStock class or updated stock
        '''
        item_name = input('Podaj nazwę produktu: ')
        try:
            amount = int(input('Ile sztuk dodajesz: '))
        except ValueError:
            return print('To nie jest liczba całkowita.')
        item_present = self.dry_stock_name_check(item_name)
        if item_present:
            item_present.stock += amount
        else:
            item_type = input('Podaj rodzaj (karma, akwarium, akcesoria) produktu: ')
            item_brand = input('Podaj markę produktu: ')
            Store.dry_stock_list.append(DryStock(item_name, item_type, item_brand, amount))

    def drystock_display(self) -> None:
        '''
        Prints dry stock using magic method __str__
        :return: Dry stock
        '''
        for item in Store.dry_stock_list:
            print(item)

    def dry_stock_sale(self) -> None:
        '''
        Checks for desired item in stock:
            If not available prints out information.
            If available takes user input of how many items he would like to buy.
                If not available prints out information
                If available deducts quantity from stock, adds information on loyalty card if possible.
        :return: updated stock and loyalty card operations
        '''
        item_for_sale = self.dry_stock_name_check()
        if item_for_sale:
            try:
                amount = int(input('Ile sztuk sprzedajesz: '))
            except ValueError:
                return print('To nie jest liczba całkowita.')
            if item_for_sale.stock >= amount:
                item_for_sale.make_a_sale(amount)
                self.loyalty_points_incrementator(amount, item_for_sale.name)
            else:
                print(f'Nie masz wystarczającej liczby {item_for_sale.name}')
        else:
            print('Nie ma tego produktu na stanie.')

    def add_new_loyalty_card(self) -> None:
        '''
        :return: creates a new instance of LoyaltyCard and stores it in a card_list
        '''
        customer_phone = input('Podaj numer telefonu klienta: ')
        Store.card_list.append(LoyaltyCard(customer_phone))

    def loyalty_points_incrementator(self, points_amount: int, item_name: str) -> None:
        card_used = self.card_retriever()
        if card_used:
            card_used.add_points(points_amount)
            print(f'{points_amount} punkty dodane, całkowita ilość punktów: {card_used.collected_points}')
            card_used.history_update(item_name, points_amount, card_used.collected_points)
        else:
            print('Do tej transakcji nie wykorzystano karty lojalnościowej')

    def card_retriever(self) -> object:
        '''
        Takes loyalty card number, checks if it's already created. If yes returns card object
        :return: card object
        '''
        card_no = input('Podaj numer karty lojalnościowej (zostaw puste, jeżeli nie ma karty): ')
        try:
            card_no = int(card_no)
        except ValueError:
            return print('To nie jest liczba całkowita.')
        for card in Store.card_list:
            if card.card_idx == card_no:
                return card

    def show_card_history(self) -> None:
        '''
        Shows transaction history for loyalty card instance
        :return: prints transaction history
        '''
        card_no = self.card_retriever()
        if card_no:
            print(f'Stan punktów: {card_no.collected_points}')
            [print(f'Dnia: {element[0]} kupiłeś {element[2]}szt {element[1]}. Liczba pkt po transakcji: {element[3]}')
             for element in card_no.purchase_history]
        else:
            print('Nie ma karty o takim numerze.')

    def exit_program(self):
        DataManager(Store.livestock_list, 'livestock').data_writer()
        DataManager(Store.dry_stock_list, 'drystock').data_writer()
        DataManager(Store.card_list, 'customercards').data_writer()

    def main(self):
        while True:
            menu_choice = self.menu_interface()
            if menu_choice == '0':
                self.exit_program()
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
            elif menu_choice == '7':
                self.add_new_loyalty_card()
            elif menu_choice == '8':
                self.show_card_history()
                # TODO Remove / reformat below commands
            elif menu_choice == '9':
                self.dict_converter()
            elif menu_choice == '10':
                self.data_loader()


if __name__ == '__main__':
    Store()
