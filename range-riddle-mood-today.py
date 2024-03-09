import random

'''
Write a program that simulates different moods for each day of the week.
Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm".
Using the range() function, loop through the days of the week and for each
day, randomly select a mood from the list and print it. Ensure that your
program includes the use of the random module to select the mood.
'''

days = ["Mondays", "Tuesdays", "Wednesdays", "Thursdays", "Fridays", "Saturdays", "Sundays"]
moods = ["Lethargic", "Ambivalent", "Cranky", "Frustrated", "World weary"]

# Create a dictionary to store the mood for each day
mood_dict = {}

for day in days:
    random_mood = random.choice(moods)
    mood_dict[day] = random_mood


for day, mood in mood_dict.items():
    print(f"{day}: {mood}")

# I don't know enough about dictionaries to know why this is the only way that the code seems to
# work or why you need to use variable.items(), but there it is.