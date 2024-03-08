'''
The range() function is used to generate a sequence of numbers. However, the code snippet
provided does not work as intended. Your task is to identify why the loop might not be
executing and correct the code so that it prints numbers from 5 down to 3.
'''
# original code:
# for i in range(5, 2):
#     print(i)  

for i in range(5, 2, -1):
    print(i)

'''
For the above code, since you're counting down, you need to add a step of -1. Without that,
it will try to count up, but can't since as originally written, it was meant to start at 5
and stop at 2 which isn't doable.
'''