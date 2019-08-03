#This is a program to swap first and last digit of a number using a for loop.
print('This is a program to swap first and last digit of a number using a for loop.')
value_n = input('Enter a number : ')
print(' ')    # printing blank line.

list_of_digits = []    # list decleration.
swapped_result = ''    # string decleration.
length_of_value_n = len(value_n)    # calculating length of entered string.

for x in range(0,length_of_value_n):
    insert_this = value_n[x]    # stored string element in insert_this variable using index of string.
    list_of_digits.append(insert_this)    # adding elements in a list.

length_of_list_of_digits = len(list_of_digits)    # calculating length created list.
    
tmp = list_of_digits[-1]    # last digit from list goes into tmp.
list_of_digits[-1] = list_of_digits[0]    # first digit from list goes on last position of list.
list_of_digits[0] = tmp    # tmp value goes on first position of list.    

for x in range(0,length_of_list_of_digits):
    swapped_result = (swapped_result + list_of_digits[x])    # regenerated the string from list.
   
print('Before swapping : ', value_n)    # number before swapping.
print('After swapping : ', swapped_result)    # number after swapping.

