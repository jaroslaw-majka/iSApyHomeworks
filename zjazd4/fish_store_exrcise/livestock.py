class FishStock:
    def __init__(self, name: str, origin: str, amount: int, freshwater: bool):
        '''
        Args:
            name (str): fish name
            origin (str): where this fish originates from
            amount (int): available stock
            freshwater (bool): True if fish is freshwater, False if it's saltwater
        '''
        self.name = name
        self.origin = origin
        self.amount = amount
        self.freshwater = freshwater

    def make_a_sale(self, amount: int) -> int:
        '''
        Deducts sold quantity from available stock
        :param amount: quantity of items sold that need to be deducted from available stock
        :return: updated stock
        '''
        if isinstance(amount, (int, float)):
            self.amount -= amount
        else:
            print('Podana ilość musi być liczbą')
