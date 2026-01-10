from core import database

def check_balance(card_number):
    user = database.get_user(card_number)
    return user["balance"]

def withdwaw(card_number, amount):
    user = database.get_user(card_number)

    if amount <= 0:
        print("Error: Amount must be positive.")
        return None
    
    elif user["balance"] >= amount:
        user["balance"] -= amount
        return user["balance"]
    
    else:
        print("Error: Insufficient funds.")
        return None