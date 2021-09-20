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

    def print_dry_stock_list(self):
        for key, value in vars(self).items():
            print(key, value)

    # alternative for above stock displayer
    def __str__(self):
        return f'Nazwa: {vars(self)["item_name"]}, ' \
               f'Producent: {vars(self)["brand"]}, ' \
               f'Ilość sztuk: {vars(self)["stock"]}'

    def make_a_sale(self, amount):
        if isinstance(amount, (int, float)):
            self.stock -= amount
        else:
            print('Podana ilość musi być liczbą')
