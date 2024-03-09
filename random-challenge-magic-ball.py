import random

'''
Create a Magic 8-Ball program that provides random advice. Use random.choice()
to select a random response from a list of possible answers every time the user
asks a question.
'''

responses = [
    "Hell no.",
    "Not today, Satan.",
    "Ask again once Jupiter goes into retrograde.",
    "Count on it like you can count on an abacus.",
    "Definitely maybe.",
    "Outlook murky, like a politician's morals.",
    "Yeah, probably. I don't know.",
    "Without a doubt, except the one.",
    "As a blind man sees it, sure."
]

while True:
    question=input("Ask the magic 8-ball a 'yes or no' question: (Press enter to quit.) ")
    answer = random.choice(responses)
    if question=="":
        print("Thanks for playing!")
        break
    print(f"The all-knowing Magic 8-ball says: {answer}")