from_here = int(input('Enter number from where to start prime number search : '))
to_here = int(input('Enter number to search till there : '))

def prime_or_not(N):    # declared function named as prime_or_not.
    if (N > 1):    
        for x in range(2, N):    
            if ((N % x) == 0):
                return False
                break     
        else:
            return True
    else:
        return False


for check_this in range(from_here, to_here):
    if not (prime_or_not(N = check_this)):
        pass
    else:
        print('%d is a prime number between (%d and %d)' % (check_this, from_here, to_here))
    