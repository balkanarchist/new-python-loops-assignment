import random

# Create a game where a player has to guess the random item picked by the computer from a list. 
# Use random.choice() to select the item and take the user's guess via input. 
# Provide feedback on whether they guessed correctly or not.

japanese_foods = ["unadon", "yakitori", "fugu tempura", "natto", "sushi", "gyoza", "okonomiyaki", "onigiri"]

random_item = random.choice(japanese_foods)

while True:
    guess = input("Guess the Japanese food (or 'quit' to exit): ")
    if guess == random_item:
        print(f"Yatta! You guessed it right. The item was {random_item}.")
        break
    elif guess == "quit":
        print(f"The correct item was {random_item}. Thanks for playing!")
        break
    else:
        print("Oops! That's not correct. Try again!")