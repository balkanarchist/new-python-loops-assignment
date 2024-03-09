import random

'''
Implement a number guessing game where the computer randomly selects
a number within a range, and the player has to guess it. Use random.randint()
to generate the number and give the player a hint after each incorrect guess 
whether their guess was too high or too low.
'''

minimum = 1
maximum = 42
secret_number = random.randint(minimum, maximum)

print(f"Are you ready? I've chosen a (whole) number between {minimum} and {maximum}. Can you guess what it is?")

while True:
    user_guess = int(input("Enter your guess: "))
    if user_guess == secret_number:
        print(f"Congratulations! You guessed it. The secret number was {secret_number}.")
        break
    elif user_guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")