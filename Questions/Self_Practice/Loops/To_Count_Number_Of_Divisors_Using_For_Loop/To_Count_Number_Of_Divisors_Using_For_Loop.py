# To count no. of divisors for a number. 
print('To count no. of divisors for a number.')
import math    # importing math library. 

cnt = 0 # counter set to 0.

N = int(input("Enter a number : "))    # asking user for input.

for i in range(1, (int(math.sqrt(N)) + 1)) :     
    if (N % i == 0) : 
        if (N / i == i) : 
            cnt = cnt + 1
        else : 
            cnt = cnt + 2
print(cnt)