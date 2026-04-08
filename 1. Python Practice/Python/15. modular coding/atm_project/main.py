from core import auth
from core import transactions

def main():
    print("=== WELCOME TO PYTHON BANK ===")

    card = input("Enter Card Number : ")
    pin = input("Enter PIN : ") 

    if auth.login(card, pin):
        print(f"\nLogin Successful! Welcome, User {card}")

        while True:
            print("\n1. Check Balance")
            print("2. Withdraw Balance")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                bal = transactions.check_balance(card)
                print(f"Your Balance: ${bal}")

            elif choice == "2":
                amount = float(input("Amount to withdraw : "))
                new_bal = transactions.withdwaw(card, amount)

                if new_bal is not None:
                    print(f"Please take your cash. New Balance : ${new_bal}")
            
            elif choice == "3":
                print("Thank you for using Python Bank.")
                break
            else:
                print("Invalid Option!")
    else:
        print("\nLogin Failed! Wrong Card or PIN.")
        

if __name__ == "__main__":
    main()