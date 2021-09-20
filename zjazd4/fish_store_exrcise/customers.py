class LoyaltyCard:
    next_card_idx = 1

    def __init__(self, phone_no):
        self.card_idx = LoyaltyCard.next_card_idx
        self.collected_points = None
        self.customer_phone = phone_no
        LoyaltyCard.next_card_idx += 1
