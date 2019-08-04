n = int(input())
a = list(map(int, input().split()))
xori = 0


for i in range(n):
   xori = xori ^ a[i]

   
print(xori)