#This is a program to print sum of all even numbers between 1 to n using while loop.
print('This is a program to print sum of all even numbers between 1 to n using while loop.')
value_n = int(input('Enter a value for n : '))

x = 1   # setting counter value to 1. 
sum = 0    # setting sum value to 1.

while x < value_n:  # while loop runs till x value is less then value_n. 
    x = x + 1   # counter value incrimented by one here.
    if((x%2) == 0): # this will execute if remender is ezual to zero.
        sum = sum + x # previous value of sum will be added to x and is stored stored again in sum 
        
print('Sum is : ',sum)    # printing value of sum.
        
        
