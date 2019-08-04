#This is a program to print all natural numbers from 1 to n in reverse order using while loop.
print('This is a program to print all natural numbers from 1 to n in reverse order using while loop.')
value_n = int(input('Enter a value for n :'))
x = (value_n + 1)   # setting counter to (value_n + 1). 
while x > 1:  # while loop runs till x value is greater then (value_n+1). 
    x = x - 1   # counter value decrimented by one here.
    print(x)    # printing counter value
        
        
