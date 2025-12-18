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
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    def create_pin(self):
        user_pin = input("Enter your PIN : ")
        if len(user_pin) >= 4:
            self.pin = user_pin
            print("PIN created successfully!")

            user_balance = input("Enter your Balance : ")
            self.balance = user_balance
            print("Balance Depostite successfully!")
        else:
            print("PIN will be at least 4 character. Please try again!")

        
        self.menu()

atm = AtmMachine()
        