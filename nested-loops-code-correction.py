'''
The code below is intended to print a 3x3 grid of asterisks. However, the
current output is not as expected. Identify the logical errors in the nested
loops and correct the code so that it prints the grid correctly, with each
row of asterisks on a new line.

for i in range(3):
    for j in range(3):
        print("*")
    print("\\n")
'''

for i in range(3): #the row value
    for j in range(3): #the column value
        print("*")
    print("\\n")

# I think identifying a variable(n) and setting its value to 3 will show that we only want 3 rows
# and 3 columns of asterisks. Next, I'd replace the (3) inside the ranges with n. Next, with the first
# print statement, add a comma then "(end ="")" to show that that's the end of each line. Finally,
# on the last print statement, just leave that blank. It's there to exit the outer loop (whatever
# that really means. TBH, I'm not sure, but the code should work now as expected.)

print() #added here for readability and to separate the two versions of the code

n = 3

for i in range(n):
    for j in range(n):
        print("*", end =" ")
    print()