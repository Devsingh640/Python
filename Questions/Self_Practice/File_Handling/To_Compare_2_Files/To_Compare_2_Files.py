print(' ')    # to print a blank line.
file_1 = open('test_1.txt', mode ='w')    # to create a new file and open it in write mode.
file_1.write('Hello World.')    # writing into file.
file_1.close()    # close file once its work is done.
print(' ')    # to print a blank line.

print(' ')    # to print a blank line.
file_2 = open('test_2.txt', mode ='w')    # to create a new file and open it in write mode.
file_2.write('How Are You.')    # writing into file.
file_2.close()    # close file once its work is done.
print(' ')    # to print a blank line.

file_1 = open('test_1.txt', mode = 'r')    # opening file in read mode.
file_2 = open('test_2.txt', mode = 'r')    # opening file in read mode.
contents_of_file_1 = file_1.read()    # storing file content into a variable.
contents_of_file_2 = file_2.read()    # storing file content into a variable.
file_1.close()    # close file once its work is done.
file_2.close()    # close file once its work is done.

if(contents_of_file_1 == contents_of_file_2):
    print('Contents of these files are same.')
    print(' ')    # to print a blank line.
    print('File_1 contents are : \n', contents_of_file_1)
    print(' ')    # to print a blank line.
    print('File_2 contents are : \n', contents_of_file_2)
    
else:
    print('Contents of these files are not same.')
    print(' ')    # to print a blank line.
    print('File_1 contents are : \n', contents_of_file_1)
    print(' ')    # to print a blank line.
    print('File_2 contents are : \n', contents_of_file_2)    
