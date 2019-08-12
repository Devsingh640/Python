# To print rectangle star pattern.

rows = int(input('Enter number of rows : '))    # taking input for rows.
columns = int(input('Enter number of columns : '))    # taking input for columns.

space = 0    # d

for i in range(0, rows):
    
    if(space == 0):
        pass    # to pass this block without any error.
    else:
        for i in range(0, space):
            print(' ', end=' ') # this will print space.
    
    for w in range(0, columns):
        print('*', end=' ')
    
    space = space + 1    # incrementing space counter.
    
    print(' ')    # append blank space et end and cursor moves to next line.
    



    
5