class DryStock:
    def __init__(self, item_name, item_type, brand, stock):
        '''
        Args:
            item_name (str): name of the item
            item type (str): eg. food, aquarium, accessories
            brand (str): item brand
            stock (int): item amount
        '''
        self.item_name = item_name
        self.item_type = item_type
        self.brand = brand
        self.stock = stock

    def __str__(self) -> str:
        '''
        Overwrites the way data is presented when Store.drystock_display func is called
        :return: string formatting for list item display
        '''
        return f'Nazwa: {vars(self)["item_name"]}, ' \
               f'Producent: {vars(self)["brand"]}, ' \
               f'Ilość sztuk: {vars(self)["stock"]}'

    def make_a_sale(self, amount: int) -> int:
        '''
        Deducts sold quantity from available stock
        :param amount: quantity of items sold that need to be deducted from available stock
        :return: updated stock
        '''
        if isinstance(amount, (int, float)):
            self.stock -= amount
        else:
            print('Podana ilość musi być liczbą')
