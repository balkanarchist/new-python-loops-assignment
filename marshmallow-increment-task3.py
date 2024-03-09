'''
Create a while loop where an off-by-one error could occur due to the
placement of the increment operation. Your loop should aim to fill a 
bag with exactly 10 marshmallows, but due to the off-by-one error, it 
either has too few or too many. Correct the error and explain the
importance of increment placement in preventing such errors.
'''

marshmallows_in_bag = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")