class LoyaltyCard:
    next_card_idx = 1

    def __init__(self, phone_no):
        self.card_idx = LoyaltyCard.next_card_idx
        self.collected_points = 0
        self.customer_phone = phone_no
        self.purchase_history = []
        LoyaltyCard.next_card_idx += 1

    def add_points(self, points_to_be_added: int) -> None:
        """
        :param points_to_be_added: amount of points that will be added to this cards balance
        :return: current points balance
        """
        if isinstance(points_to_be_added, int):
            self.collected_points += points_to_be_added

    #TODO History:
        # History should save the date, name of the item and quantity bought. As well as after purchase points status.
