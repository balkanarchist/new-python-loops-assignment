'''
Modify the code from Task 1 by moving the increment operation to the end
of the loop. Predict what the output will be and then run the code to check
your prediction. Discuss the differences in the output and how the placement
of the increment affects the loop's behavior.
'''

marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1

# The number should increase as expected from 0 up to 4 because the +=1 line is added after
# the print statement. Because the increment comes after the print statement, it will never
# output as having 5 marshmallows because the code is meant to stop when the number is no
# longer less than 5 (i.e., stopping at 4).