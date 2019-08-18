print('To calculate total no of even and odd elements of a list.')
print('')

a = [-1, 2, -3, 4, -5, 6 , -7]

even_counter = 0
odd_counter = 0

for el in a:
    if ((el % 2) == 0):
        even_counter = (even_counter + 1)
    else:
        odd_counter = (odd_counter + 1)

print('Total no of even number : ', even_counter)
print('Total no of odd number : ', odd_counter)