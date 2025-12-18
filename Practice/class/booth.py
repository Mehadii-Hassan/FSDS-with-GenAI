class AtmMachine:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Welcome to ATM Machine : 
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balence
            4. Press 4 to withdraw
            5. Anything to exit
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.balance_withdraw()
        else:
            exit()
    
    def create_pin(self):
        user_pin = input("Enter your PIN : ")
        if len(user_pin) >= 4:
            self.pin = user_pin
            print("PIN created successfully!")

            user_balance = float(input("Enter your Balance : "))
            self.balance = user_balance
            print("Balance Depostite successfully!")
        else:
            print("PIN will be at least 4 character. Please try again!")        
        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old PIN : ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN : ")
            if len(new_pin) >= 4:
                self.pin = new_pin
                print("PIN created successfully!")
            else:
                print("PIN will be at least 4 character. Please try again!")
        else:
            print("Your PIN is incorrect, please try again!")
        self.menu()

    def check_balance(self):
        user_pin = input("Enter your PIN : ")
        if user_pin == self.pin:
            print(f"Your Balance is BDT : {self.balance}")
        else:
            print("Your PIN is incorrect, Please try again!")
        self.menu()

    def balance_withdraw(self):
        user_pin = input("Enter your PIN : ")
        if user_pin == self.pin:
            amount = float(input("Enter your amount to withdraw : "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have withdrawn BDT : {amount}. Your new balance is BDT : {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Your PIN is incorrect, Please try again!")
        self.menu()

atm = AtmMachine()