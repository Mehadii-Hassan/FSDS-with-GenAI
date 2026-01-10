# A mock database of users
# Format : "Card Number" : {"pin" : "PIN", "balance" : "Amount"}

users = {
    "1111" : {"pin" : "1234", "balance" : 5000},
    "2222" : {"pin" : "9995", "balance" : 1000},
    "3333" : {"pin" : "6248", "balance" : 500},
    "4444" : {"pin" : "8525", "balance" : 100}
}

def get_user(card_number):
    """Fetches user data if the card exists."""
    return users.get(card_number)