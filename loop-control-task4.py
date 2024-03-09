# Implement a while loop where you want to temporarily skip the implementation
# of a condition but plan to add more code later.
# Use the pass statement as a placeholder.
# Describe the use of pass in a loop and when it might be useful.

num = 1
while num <= 16:
    if num % 3 == 0:
        num += 1
        continue
    if num == 13:
        pass
    print(num, end=" ") #using end just to make the output more readable
    num += 1

'''
Use the pass statement as a placeholder - i.e., when you know you want something to happen at
that point in the code, but you haven't decided what just yet. Using pass will tell Computer-San
to just ignore that bit for now. Not using the pass statement will result in an error.
'''