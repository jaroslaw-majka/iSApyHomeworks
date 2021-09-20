class LoyaltyCard:
    next_card_idx = 1

    def __init__(self, phone_no):
        self.card_idx = LoyaltyCard.next_card_idx
        self.collected_points = None
        self.customer_phone = phone_no
        LoyaltyCard.next_card_idx += 1

    #TODO Add points incrementation when a sale is made (1 item = 1 point)
        # Need to create a function in store.py and make it possible to add a card idx when a purchase is made.
        # Leaving field empty will result with no loyalty card operations (no points added, no history created)

    #TODO History:
        # History should save the date, name of the item and quantity bought. As well as after purchase points status.
