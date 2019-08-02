# This is a program to print all even number between 1 to 100 using while loop.
print('This is a program to print all even number between 1 to 100 using while loop.')

x = 1  # setting counter to 1. 

while (x < 100):  # while loop runs till x is less than 100 and its remainder is 0. 
    x = x + 1   # counter value incrimented by one here.
    if((x % 2) == 0):  # if remainder is 0 then execute this.
        print(x)    # printing x