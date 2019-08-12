remove_this = input('Enter the word that has to be removed : ')
file = open('test.txt', mode = 'w')
file.write('i am first line.\ni am second line.\ni am third line.')
file.close()

file = open('test.txt', mode ='r')
print('=========================================================')
for line in file:
    print('LINE IS : ', line)
    line_length = len(line)
    print('LINE LENGTH IS :', line_length )
    
    using_split = line.split()
    print('SPLIT RESULT :',using_split)
    split_length = len(using_split)
    print('SPLIT LENGTH :', split_length)
    print('=========================================================')
    
    for x in range(0, split_length-1):
        if(remove_this == using_split[x]):
            using_split.pop(x)
            print(using_split)
        else:
            pass
        
