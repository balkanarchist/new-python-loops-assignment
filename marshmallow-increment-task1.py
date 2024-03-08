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
# The output should be a repeated line of the text in the print statement, with each line
# increasing the number of marshmallows by 1 until it gets to 5 at which point it will stop.
# The number should increase as expected because the +=1 line is added before the print statement.