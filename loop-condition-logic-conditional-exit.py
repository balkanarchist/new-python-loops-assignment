'''
Modify the infinite loop from Task 1 to include a condition that will
eventually be true and remove the break statement. The loop should
terminate naturally once the condition is met. Discuss how the loop 
condition determines when the loop exits.
'''

# original code below:
# counter = 0
# while True:
#     print(f"Looping through iteration {counter + 1}.")
#     counter += 1
#     if counter >= 5:
#         break

# print("Fini.")

# revised code below:
counter = 10
while counter !=1:
    print(f"Counting down to {counter - 1}.")
    counter -= 1

'''
In the original code, the condition was such that it would keep looping (from zero) until it reached 5
at which point, it was told to stop, because of the break statement.
In the revised code, the condition was revised so that no break would be needed. To achieve this, I
reversed the order for a countdown-themed iteration with the condition that it was meant to iterate
until it counted down to 1 at which point the condition would no longer be true, and the code would
thus stop without the need for a break statement.
'''