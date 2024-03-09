import random

# Simulate shuffling a deck of cards using random.shuffle().
# Create a list representing a deck of cards, then shuffle it and print the shuffled deck.
# Discuss how random.shuffle() can be used in game development or other applications.

suits = ["♣", "♢", "♡", "♠"] # testing use of non-traditional characters in code
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = [(rank, suit) for rank in ranks for suit in suits]

random.shuffle(deck)

for card in deck:
    print(f"{card[0]}{card[1]}", end=" ")
print("\n")

'''
The shuffle function will return a list in a shuffled order, changing (and replacing)
the sequence of their positions. In general, this can be useful for testing purposes
if you want to see how data set items will react to different positions.
In terms of gaming and/or simulations, for example, you might need for items to be
shuffled in order to prevent any biases or patterns forming among the items which may
occur if they stay in a static form.
The advantage of shuffling is most readily understood with cards, as in this example,
because without shuffling, if you go through several rounds, a player may be able to 
remember (at least in part) the order of the cards, giving him an unfair advantage over
other players.
'''