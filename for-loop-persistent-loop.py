'''
Implement a for loop that searches for a specific number in a list
of numbers. If the number is found, use break to exit the loop. If
the loop completes without finding the number, an else clause should
be used to print a message stating that the number was not found. This
task will help you understand how to use the else clause in conjunction
with the break statement in loops.
'''

my_list = [2, 7, -13, 42, 25]
specific_number = -13

def number_to_search(specific_number, number_list): #not clear on functions, but this seems to work
    for num in number_list:
        if num == specific_number:
            print(f"Number {specific_number} found in the list.")
            break
    else:
        print(f"Number {specific_number} was not found in the list.")

number_to_search(specific_number, my_list) #not sure why this goes on the bottom, but it works this way