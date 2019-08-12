# To print rectangle star pattern.

rows = int(input('Enter number of rows : '))    # taking input for rows.

space = 0   
c = 0

for i in range(0, rows):
     
    if(space == 0):
        pass    # to pass this block without any error.
    else:
        for i in range(0, space):
            print(' ', end=' ') # this will print space.
    
    for w in range(0, (rows - c)):
        print('*', end=' ')
    
    space = space + 1    # incrementing space counter.
    
    c = c + 1
    
    print(' ')    # append blank space et end and cursor moves to next line.
    



    
5