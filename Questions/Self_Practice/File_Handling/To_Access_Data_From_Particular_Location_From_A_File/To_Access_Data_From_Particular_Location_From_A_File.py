num_string_for_file_1 = '12345644455544444445333333333333333333333333'



print(' ')    # to print a blank line.
file_1 = open('test_1.txt', mode ='w')    # to create a new file and open it in write mode.
file_1.write(num_string_for_file_1)    # writing user entered number into file.
file_1.close()    # close file once its work is done.
print(' ')    # to print a blank line.

file_1 = open('test_1.txt', mode = 'r')    # opening file in read mode.
contents_of_file_1 = file_1.read()    # storing file content into a variable.
file_1.close()    # close file once its work is done.

file_1 = open('test_1.txt', mode ='r')    # to create a new file and open it in write mode.

cursor_position_1 = file_1.seek(5, 0)    # 5 is offset and 0 is reference from front.
cursor_position_2 = file_1.seek(0, 1)    # 0 is offset and 1 is reference from previous position.
cursor_position_3 = file_1.seek(0, 2)    # EOF.

read_1 = file_1.read(cursor_position_1)
read_2 = file_1.read(cursor_position_2)
read_3 = file_1.read(cursor_position_3)

print('new Cursor position: ', cursor_position_1,', data: ', read_1,)
print('new Cursor position: ', cursor_position_2,', data: ', read_2,)
print('new Cursor position: ', cursor_position_3,', data: ', read_3,)

file_1.close()    # close file once its work is done


