

def total_character_and_alphabets(length_of_read_string):
    alphabets = 0
    characters = 0
    for x in range(0, (length_of_read_string)):
        a =  ord(contents_of_file_1[x])
        if((a >= 65)  and (a <= 90)):
            alphabets = (alphabets + 1)
        elif((a >= 97) and (a <= 122)):
            alphabets = (alphabets + 1)
        else:
            pass
        characters = (characters + 1)
    return(alphabets,characters)
    
    
def total_words(length_of_read_string):
    word = 0
    previous = 32
    for x in range(0, (length_of_read_string)):
        present =  ord(contents_of_file_1[x])
        if((present == 32) & (previous == 32)):
            pass
        elif((present != 32) & ( previous == 32)):
            word = (word + 1) 
        elif((present != 32) & (previous != 32)):
            pass
        else:
            pass
        previous = present 
    return(word)
    
    
print(' ')    # to print a blank line.

file_1 = open('test_1.txt', mode ='w')    # to create a new file and open it in write mode.
file_1.write('Nullam a lobortis velit, in gravida ante.\nNullam rhoncus diam nec metus tristique porttitor.\nProin tempus, dolor quis pretium elementum, nunc dui tempus dolor. \nAliquam eu orci nec tortor fermentum volutpat. \nLorem ipsum dolor sit amet, consectetur adipiscing elit. \nNam non risus at quam convallis feugiat in vitae nisi. \nInteger sem felis, ornare at sagittis ac, vestibulum ut neque. \nCras diam dolor, mattis ornare placerat non, facilisis non metus. \nDuis magna nunc, laoreet sagittis libero hendrerit. \nIn sed imperdiet lacus. \nMaecenas nec felis non lectus volutpat ultricies ut id sapien. \nMauris dignissim id ligula sit amet vulputate. \nNullam id porta sem. \nPellentesque bibendum finibus viverra. \nMorbi sollicitudin diam nec eros efficitur lacinia. \n')
file_1.close()    # close file once its work is done.
file_1 = open('test_1.txt', mode = 'r')    # opening file in read mode.
contents_of_file_1 = file_1.read()    # storing file content into a variable.
file_1.close()    # close file once its work is done

length_of_read_string = len(contents_of_file_1)

(alphabets, characters) = total_character_and_alphabets(length_of_read_string)
words = total_words(length_of_read_string) 

print('Total chatacters', length_of_read_string)
print('Total alphabets', alphabets)
print('Total words', words)

print('File contains %d alphabets, %d characters, %d words.' % (alphabets, characters, words))
    

    
    
