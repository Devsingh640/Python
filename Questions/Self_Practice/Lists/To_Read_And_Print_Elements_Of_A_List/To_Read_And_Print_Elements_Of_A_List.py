print('To read and print elements of a list.')
print('')

a = [1, 2, 3, 4, 5, 6 , 7]
counter = 0

for el in a:
    print('At index %d, %d is placed.' % (counter, el))
    counter = (counter + 1)