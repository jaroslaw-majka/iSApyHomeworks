class LoyaltyCard:
    next_card_idx = 1

    def __init__(self):
        self.card_idx = None
        self.collected_points = None
        # TODO Below attribute is quoted out for testing simplicity
        # self.customer_phone = None
        LoyaltyCard.next_card_idx += 1
