print('Square star pattern.')

rows = int(input('Enter no of rows : '))

for row in range(1, (rows + 1)):
    for column in range(1,(rows + 1)):
        print('*', end=' ')
    print('')