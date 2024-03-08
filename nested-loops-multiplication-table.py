'''
Your task is to create a multiplication table for numbers 1 through
5. Use nested loops where the outer loop represents the multiplier
and the inner loop represents the multiplicand. Print the results in
a tabular format.
'''

for j in range(1, 6):
    for k in range(1,6):
        print(j * k, end = "\t")
    print("\n")