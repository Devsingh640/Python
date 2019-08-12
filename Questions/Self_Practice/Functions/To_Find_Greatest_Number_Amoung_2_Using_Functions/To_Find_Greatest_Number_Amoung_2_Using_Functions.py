first_num = int(input('Enter first number : '))
second_num = int(input('Enter second number : '))


def greater_is(a, b):    
    if(a > b):
        return(a)    # if a is greater a will be send back.
    else:
        return(b)    # if b is greater a will be send back.


greatest = greater_is(b = second_num, a = first_num)    # called function and passed 2 values to it.


print('\nGreatest amoung the two number is : ', greatest)
