a = []
N = int(input(" "))


for x in range(1, N + 1):
    element = int(input(" "))
    a.append(element)
    print(a)


for x in range(0, N + 1):
    if a[x] in a:
        d = a.count(a[x])
        print(d)