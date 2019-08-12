check_this = int(input("Enter a number to check if it is prime or not : "))

def prime_or_not(N):    # declared function named as prime_or_not.
    if (N > 1):    
        for x in range(2, N):    
            if ((N % x) == 0):
                print("NO")
                break     
        else:
            print("YES")
    else:
        print("NO")
        
prime_or_not(N = check_this)    # calling function.