num_string_for_file_1 = '1234567891642378567832169237521827463548324758123758273561283564'

def even_or_odd(a):    
    if((a % 2) == 0):
        return(False)    # if a is even true will be send back.
    else:
        return(True)    # if b is odd false will be send back.

print(' ')    # to print a blank line.
file_1 = open('test_1.txt', mode ='w')    # to create a new file and open it in write mode.
file_1.write(num_string_for_file_1)    # writing user entered number into file.
file_1.close()    # close file once its work is done.
print(' ')    # to print a blank line.


file_1 = open('test_1.txt', mode = 'r')    # opening file in read mode.
contents_of_file_1 = file_1.read()    # storing file content into a variable.
file_1.close()    # close file once its work is done.

length_of_read_string = len(contents_of_file_1)

for x in range(0,length_of_read_string):
    num = int(num_string_for_file_1[x])
    
    if not even_or_odd(a = num):
        file_o = open('test_even.txt', mode ='a')    # to create a new file and open it in write mode.
        file_o.write(num_string_for_file_1[x])    # writing user entered number into file.
        file_o.close()    # close file once its work is done.
    else:
        file_e = open('test_odd.txt', mode ='a')    # to create a new file and open it in write mode.
        file_e.write(num_string_for_file_1[x])    # writing user entered number into file.
        file_e.close()    # close file once its work is done.



    
    
