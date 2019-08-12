# To print rectangle star pattern.

rows = int(input('Enter number of rows : '))    # taking input for rows.

space = rows - 1

for i in range(1, rows):
    space = space - 1
    for i in range(0, space):
        print(' ', end=' ')
    for w in range(0, rows):
        print('*', end=' ')
    print(' ')
    



    
