import math
cnt = 0
N = int(input(""))

for i in range(1, int(math.sqrt(N)) + 1) : 
    if (N % i == 0) : 
        if (N / i == i) : 
            cnt = cnt + 1
        else : 
            cnt = cnt + 2
print(cnt)