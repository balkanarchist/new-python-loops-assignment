import random

'''
Develop a game where the computer randomly picks a card from a deck, and the player has to
guess the suit or the rank. Use random.choice() to select the card, and then check if the 
player's guess matches the suit or rank of the chosen card.
'''
# First, set up the cards, then do player input with if/else
# Use capital letters for suits to match capitals in rank, then can add .capitalize()
# Looks like you only need to give the player one guess before revealing answer

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = [(rank, suit) for rank in ranks for suit in suits] #combine the other lists for random choice

def main():
    print("Let's see if you can guess the card!")
    while True:
        random.shuffle(deck)
        chosen_card = random.choice(deck)
        chosen_rank, chosen_suit = chosen_card
        
        player_guess = input("Guess the suit or rank (enter 'suit' or 'rank'): ").lower()
        if player_guess not in ["suit", "rank"]:
            print("Invalid input. Please enter 'suit' or 'rank'.")
            continue
        
        if player_guess == "suit":
            correct_answer = chosen_suit
        else:
            correct_answer = chosen_rank
        
        player_answer = input(f"Enter your guess: ").capitalize() #in case user uses a lowercase letter
        if player_answer == correct_answer:
            print("Congratulations! You guessed correctly.")
        else:
            print(f"Sorry, the correct answer was {correct_answer}.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            print("Suit yourself! Goodbye.")
            break

if __name__ == "__main__": # Still not clear on why this is needed, except that because a function was called
    main()