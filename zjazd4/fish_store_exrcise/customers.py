class LoyaltyCard:
    next_card_idx = 1

    def __init__(self):
        self.card_idx = None
        self.collected_points = None
        LoyaltyCard.next_card_idx += 1
