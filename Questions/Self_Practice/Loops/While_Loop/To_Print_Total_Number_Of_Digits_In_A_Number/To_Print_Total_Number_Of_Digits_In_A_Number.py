#This is a program to print total no of digits in a number using a while loop.
print('This is a program to print total no of digits in a number using a while loop.')
value_n = int(input('Enter a number is not starting with 0 : '))

counter = 0    # setting counter to 0 that will hold no of digits count.

while True:    # infinite loop. 
    a = int(value_n / 10)    # calculating floor value.
    value_n = a    # calculated floor value is stored in value_n.
    
    if(a != 0):    # this will be executed if a is not eaual to 0.
        counter = counter + 1    # incrementing counter.
    else:
        counter = counter + 1    # incrementing counter.
        break    # this will break infinite loop.
    
print(" ")    
print(counter)    # printing count of digits.