num = int(input('Enter first number : '))


def even_or_odd(a = num):    
    if((a % 2) == 0):
        return(False)    # if a is even true will be send back.
    else:
        return(True)    # if b is odd false will be send back.


if not even_or_odd():
    print('Entered number is even')
else:
    print('Entered number is odd')


