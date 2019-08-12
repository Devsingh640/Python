# To print rectangle star pattern.

rows = int(input('Enter number of rows : '))    # taking input for rows.
columns = int(input('Enter number of columns : '))    # taking input for columns.


for i in range(0, rows):
    for w in range(0, columns):
        print('*', end=' ')
    
    print(' ')
    
