import math

N = int(input(""))

if (N > 1):    
    for x in range(2, N):    
        if ((N % x) == 0):
            print("NO")
            break     
    else:
        print("YES")
else:
    print("NO")