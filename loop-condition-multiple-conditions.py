# Create a while loop that continues to run as long as multiple conditions are true.
# Use the and or or operators to combine conditions.
# Describe how combining conditions can create more complex loop behaviors.


x = 0
y = 10
while x < 6 and y > 3:
    print(f"The value of x is {x} and the value of y is {y}.")
    x += 1
    y -= 1

'''
Combining conditions with the and operator puts extra restrictions on the code, requiring both
conditions to be true, making the loop more complex by definition. Even using the or operator
increases the complexity because whoever's writing the code may want to allow for certain
eventualities where x is valid, but y isn't (or vice-versa). This allows for more potential
outputs, thereby increasing the complexity of the code, particularly when mathematical operators
are also included.
'''