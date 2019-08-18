print('To separate even and odd elements of a list.')
print('')

a = [-1, 2, -3, 4, -5, 6 , -7]
even = []
odd = []

for el in a:
    if ((el % 2) == 0):
        even.append(el)
    else:
        odd.append(el)

print('Even list : ', even)
print('Odd list : ', odd)