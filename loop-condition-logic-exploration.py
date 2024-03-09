# Write a while loop with a condition that will never be true (an infinite loop).
# Inside the loop, print a statement.
# Then, use a break statement to exit the loop after 5 iterations.

counter = 0
while True:
    print(f"Looping through iteration {counter + 1}.")
    counter += 1
    if counter >= 5:
        break

print("Fini.")

'''
Explain the role of the loop condition and the break statement in controlling the loop execution.
A condition in a loop will determine how many times the loop should be run (i.e., in this case,
it should go through five iterations before stopping).
The break statement ensures that the code will not go beyond the point at which it's supposed to
stop, thereby avoiding a potential infinite loop situation.
'''