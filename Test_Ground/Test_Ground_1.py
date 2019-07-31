a = [1, 2, 3, 4, 5, 6, 7]

for x in range(0, len(a)):
    while (a[x] >= a[(x - 1)] & a[x] >= a[(x - 1)]):
        if (((x % 2) == 0)):
            if(a[x] >= a[x + 1]):
                c = a[x]
                y = a[(x - 1)]
                a[x] = y
                a[(x - 1)] = c