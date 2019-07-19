a = []
xoris = 0
N = int(input(" "))


for x in range(1, N + 1):
    element = int(input(" "))
    a.append(element)
    print(a)


for x in range(0, N):
        xoris = xoris ^ (a[x])
        
print(xoris)

