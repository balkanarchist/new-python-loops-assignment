'''
Create a while loop where an off-by-one error could occur due to the
placement of the increment operation. Your loop should aim to fill a 
bag with exactly 10 marshmallows, but due to the off-by-one error, it 
either has too few or too many. Correct the error and explain the
importance of increment placement in preventing such errors.
'''

marshmallows_in_bag = 0
while marshmallows_in_bag < 10:
    print("I count " + str(marshmallows_in_bag) + " marshmallows in the bag.")
    marshmallows_in_bag += 1

# The code results in an error where there are too few marshmallows in the bag, due to the
# increment being placed after the print statement. It begins with 0 because the first
# marshmallow was added after the print statement. It also stopped too early (at 9) because
# of the increment placement. Moving that before the print statement will fix the code.

print() #added for separation and readability between the two versions of the code

marshmallows_in_bag = 0
while marshmallows_in_bag < 10:
    marshmallows_in_bag += 1
    print("I count " + str(marshmallows_in_bag) + " marshmallows in the bag.")

# The code above ends when 1 marshmallows as there should be. The code has been corrected.