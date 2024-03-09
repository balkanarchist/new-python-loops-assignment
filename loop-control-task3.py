# Develop a while loop that iterates over a range of numbers.
# Use the continue statement to skip over specific numbers (e.g., multiples of 3) and print the rest.
# Explain the purpose of the continue statement and how it affects the loop's iteration.

def excluding_multiples_of_three():
    num = 1
    while num <= 16:
        if num % 3 == 0:
            num += 1
            continue
#       if num == 13: # (test) if you also wanted to skip the 13th floor specifically
#           num += 1
#           continue
        print(num, end=" ") #using end just to make the output more readable
        num += 1

# Test case:
excluding_multiples_of_three()

'''
The continue statement is meant to skip over a part of the code that is meant to be skipped over.
In the above case, we don't want to stop on floors that are evenly divisible by three, so when we
come to those, because of the continue statement, those floors will be skipped and the elevator
will resume as normal (until the next floor that's evenly divisible by three).
Continue statements are good for skipping over certain things while not stopping the code altogether.
'''