from core import database

def login(card_number, input_pin):
    user_data = database.get_user(card_number)

    if user_data:
        if user_data["pin"] == input_pin:
            return True
    return False