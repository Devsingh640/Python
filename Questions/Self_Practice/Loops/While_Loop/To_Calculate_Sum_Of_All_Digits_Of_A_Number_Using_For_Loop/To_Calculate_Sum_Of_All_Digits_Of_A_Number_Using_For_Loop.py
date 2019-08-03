#This is a program to find sum of all digits of a number using a for loop.
print('This is a program to find sum of all digits of a number using a for loop.')
value_n = input('Enter a number : ')
print(' ')    # printing blank line.

list_of_digits = []    # list decleration.
sum_is = 0    # initially sum will be 0.
length_of_value_n = len(value_n)    # calculating length of entered string.

for x in range(0,length_of_value_n):
    insert_this = int(value_n[x])    # stored int element in insert_this variable using index of string.
    list_of_digits.append(insert_this)    # adding elements in a list.

length_of_list_of_digits = len(list_of_digits)    # calculating length created list.

for x in range(0,length_of_list_of_digits):
    sum_is = (sum_is + list_of_digits[x])    # calculating sum from list.
   
print('Number entered : ', value_n)    # number entered.
print('Sum of all digits is : ', sum_is)    # printing sum_is value.
