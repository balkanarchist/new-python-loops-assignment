import random

'''
Write a program that represents your mood swings throughout a day.
The program should loop over each hour of the day and assign a random
mood from a list for each hour. However, at 'lunchtime' (which you can
define as a specific hour), the program should not print the mood. Use
the continue statement to achieve this behavior.
'''

times = ["1am", "2am", "3am", "4am", "5am", "6am", "7am", "8am", "9am", "10am", "11am", "noon", "lunchtime", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm", "11pm", "midnight"]
moods = ["Lethargic", "Ambivalent", "Cranky", "Frustrated", "World weary"]

# Create a dictionary to store the mood for each day
mood_dict = {}

for time in times:
    random_mood = random.choice(moods)
    mood_dict[time] = random_mood


for time, mood in mood_dict.items():
    if time == "lunchtime": #note that lunchtime was set at 1pm
        continue
    print(f"{time}: {mood}")

# I don't know enough about dictionaries to know why this is the only way that the code seems to
# work or why you need to use variable.items(), but there it is.