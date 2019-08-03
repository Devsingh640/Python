#This is a program to print sum of all odd numbers between 1 to n using while loop.
print('This is a program to print sum of all odd numbers between 1 to n using while loop.')
value_n = int(input('Enter a value for n : '))

x = 1   # setting counter value to 1. 
sum = 0    # setting sum value to 0.

while x < value_n:  # while loop runs till x value is less then value_n. 
    if((x%2) != 0): # this will execute if remender is not equal to zero.
        sum = sum + x # previous value of sum will be added to x and is stored stored again in sum 
    x = x + 1   # counter value incrimented by one here.    
print('Sum is : ',sum)    # printing value of sum.
        
        
