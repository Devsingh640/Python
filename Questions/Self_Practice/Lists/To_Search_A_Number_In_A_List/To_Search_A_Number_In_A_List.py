print('To search an element in a list.')
print('')

find_this = int(input('Enter number that you want to find : '))

a = [-1, 2, -3, 4, -5, 6 , -7]
counter = 0

for el in a:
    if (el == find_this):
        print('%d is placed at index %d.' % (el, counter))
    else:
        pass
    counter = (counter + 1)