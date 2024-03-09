# Write a while loop that attempts to find a specific value in a list.
# Use an else clause to print a message if the value is not found.
# Explain how the else clause works with the while loop.

my_list = [2, 7, 3.1415926535, -13, 42, 24]
target = -13
index = 0

while index < len(my_list): # use < len, I think, to cycle through each list item
    if my_list[index] == target:
        print(f"Found {target} at index {index}.")
        break
    index += 1
else:
    print(f"{target} not found in the list.")

'''
The else clause is meant to run if the if statement has run through all iterations
without encountering a break statement. It provides an output to let the user know
(in this case) that the value wasn't found in the list provided.
'''