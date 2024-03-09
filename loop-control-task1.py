# Write a while loop that attempts to find a specific value in a list.
# Use an else clause to print a message if the value is not found.
# Explain how the else clause works with the while loop.

def find_value_in_list(target_value, my_list):
    index = 0
    while index < len(my_list): # use < len, I think, to cycle through each list item
        if my_list[index] == target_value:
            print(f"Found {target_value} at index {index}.")
            break
        index += 1
    else:
        print(f"{target_value} not found in the list.")

# Test case:
my_list = [2, 7, 3.1415926535, -13, 42, 24]
target = 25
find_value_in_list(target, my_list)

'''
The else clause is meant to run if the if statement has run through all iterations
without encountering a break statement. It provides an output to let the user know
(in this case) that the value wasn't found in the list provided.
'''