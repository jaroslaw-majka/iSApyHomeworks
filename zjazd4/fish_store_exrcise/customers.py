from datetime import datetime
from typing import Tuple


class LoyaltyCard:
    next_card_idx = 1

    def __init__(self, phone_no: str):
        self.card_idx = LoyaltyCard.next_card_idx
        self.collected_points = 0
        self.customer_phone = phone_no
        self.purchase_history = []
        LoyaltyCard.next_card_idx += 1

    def add_points(self, points_to_be_added: int) -> int:
        """
        :param points_to_be_added: amount of points that will be added to this cards balance
        :return: current points balance
        """
        self.collected_points += points_to_be_added

    def history_update(self, item_name: str, item_quantity: int, points_balance: int) -> Tuple:
        '''
        :param item_name: name of the item bought
        :param item_quantity: quantity of the item bought
        :param points_balance: points balance right after this purchase
        :return: updated history list
        '''
        date = datetime.now().strftime('%d-%m-%Y')
        self.purchase_history.append((date, item_name, item_quantity, points_balance))

