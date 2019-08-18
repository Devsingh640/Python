print('To find unique elements of a list.')
print('')

a = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 1 , 7, 9, 10]

for el in a:
    count_is = a.count(el)
    if count_is == 1:
        print(el)
        