import random

jackpot = random.randint(1, 100)

guess_number = int(input("Enter your guess number: "))

counter = 1
while guess_number != jackpot:

    if guess_number < jackpot:
        print("Wrong, please guess higher number.")
    elif guess_number > jackpot:
        print("Wrong, please guess lower number.")
    else:
        print("Congratulations! You guessed the correct number.")

    guess_number = int(input("Enter your guess number: "))
    counter += 1

else:
    print("Correct Guess")
    print("Your attempt is : ", counter)