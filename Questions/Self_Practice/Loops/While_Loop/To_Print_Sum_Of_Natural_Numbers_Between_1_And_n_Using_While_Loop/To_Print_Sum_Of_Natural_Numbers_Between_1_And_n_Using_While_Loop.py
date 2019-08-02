# This is a program to print sum of all natural numbers from 1 to n using while loop.
print('This is a program to print sum of all natural numbers from 1 to n using while loop')

n = int(input('Enter value of n :')) # taking value of n from user.

x = 0  # setting counter to 0. 
sum = 0  # variable sum with initial value set to 0.

while (x < n):  # while loop runs till x is less than n. 
    x = x + 1   # counter value incrimented by one here.
    sum = sum + x # adding previous valur of sum and new value of x.

print(sum) # this will print n natural number result.