file_1 = open('test_1.txt', mode = 'w')    # opened a file in write mode.
file_1.write('This will be copied, lets check this out.')    # added some data to this file.
file_1.close()    # closed the file.

file_1 = open('test_1.txt', mode = 'r')    # opened a file in read mode.
copy_this = file_1.read()    # stored its content in a variable.
file_1.close()    # closed the file.

file_2 = open('test_2.txt', mode = 'w')    # opened a file in write mode.
file_2.write(copy_this)     # stored variable contents in this file.
file_2.close()    # closed the file.