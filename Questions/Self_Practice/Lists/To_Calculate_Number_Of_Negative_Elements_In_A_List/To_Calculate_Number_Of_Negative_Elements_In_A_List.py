print('To find total count of negative elements of a list.')
print('')

a = [-1, 2, -3, 4, -5, 6 , -7]
n_counter = 0

for el in a:
    if (el < 0):
        n_counter = (n_counter + 1)
    else:
        pass
    
print('Total number of negative elements are : ', n_counter)