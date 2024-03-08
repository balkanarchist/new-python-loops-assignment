'''
The loop below is meant to print all numbers from 1 to 10, but it stops
prematurely due to a break statement. Correct the code so that it skips
over the number 5 and continues to print the rest of the numbers.

for i in range(1, 11):
    if i == 5:
        break
    print(i)
'''

for i in range(1, 11):
    if i == 5:
        continue
    print(i)