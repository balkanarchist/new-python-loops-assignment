'''
Given the following code snippet, predict the output and then run the
code to verify your prediction. Explain why the output is what it is
based on the placement of the increment operation.

marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
'''

marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")

# The number output should start at 1 because the +=1 line is added before the print statement.
# With this in mind, it will also print 5 marshmallows because the increment happens before
# the print statement.