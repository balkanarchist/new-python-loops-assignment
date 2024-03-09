import random

'''
Simulate a mood tracker that records your mood at three different times
of the day (morning, afternoon, evening) for each day of the week. Use 
nested loops to implement this: the outer loop should iterate over the 
days, and the inner loop should iterate over the times of the day. For 
each time, randomly select a mood from a predefined list and print it.
'''

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #outer loop
time_of_day = ["morning", "afternoon", "evening"] #use random with this list; inner loop
moods = ["Lethargic", "Ambivalent", "Cranky", "Frustrated", "World weary"] #the random values

for day in days:
    for time in time_of_day:
        mood = random.choice(moods)
        print(f"{day} {time}: {mood}") #don't use the variable names here or it will output all items