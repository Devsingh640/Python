print('To read and print all negative elements of a list.')
print('')

a = [-1, 2, -3, 4, -5, 6 , -7]
counter = 0

for el in a:
    if (el < 0):
        print('%d is placed at index %d.' % (el, counter))
    else:
        pass
    counter = (counter + 1)