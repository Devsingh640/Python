#This is a program to print multiplication table for a give number using a while loop.
print('his is a program to print multiplication table for a give number using a while loop.')
value_n = int(input('Enter a value for n : '))

x = 0   # counter value set to 0.

while x in range(0,10): # this loop runs till x is greater than 10
    x = x + 1   # incrementing counter value by 1.
    multiplication_result = (value_n * x)   # multiplying user entered value with counter.
    print(value_n, ' * ', x, " = ", multiplication_result)  # printing table.

    