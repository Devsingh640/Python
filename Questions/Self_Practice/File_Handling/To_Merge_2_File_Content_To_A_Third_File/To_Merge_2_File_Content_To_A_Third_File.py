file_1 = open('test_1.txt', mode = 'w')    # opened a file in write mode.
file_1.write('I am from file 1. ')    # added some data to this file.
file_1.close()    # closed the file.
file_1 = open('test_1.txt', mode = 'r')    # opened a file in read mode.
from_file1 = file_1.read()    # stored its content in a variable.
file_1.close()    # closed the file.

file_2 = open('test_2.txt', mode = 'w')    # opened a file in write mode.
file_2.write('I am from file 2. ')    # added some data to this file.
file_2.close()    # closed the file.
file_2 = open('test_2.txt', mode = 'r')    # opened a file in read mode.
from_file2 = file_2.read()    # stored its content in a variable.
file_2.close()    # closed the file.

write_this = (from_file1 + from_file2)

file_3 = open('test_3.txt', mode = 'w')    # opened a file in write mode.
file_3.write(write_this)     # stored variable contents in this file.
file_3.close()    # closed the file.