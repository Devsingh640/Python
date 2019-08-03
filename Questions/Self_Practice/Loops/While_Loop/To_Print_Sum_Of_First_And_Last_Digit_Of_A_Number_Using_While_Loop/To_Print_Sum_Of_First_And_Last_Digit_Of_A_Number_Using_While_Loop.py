#This is a program to print sum of first and last digit of a number using a while loop.
print('This is a program to print sum of first and last digit of a number using a while loop.')
value_n = input('Enter a number is not starting with 0 : ')
length_of_value_n = len(value_n)    # calculating length of entered string.

while True:    # infinite loop. 
    if(length_of_value_n > 0):    # if something is entered then execute.
        first_digit = int(value_n[0])    # accessed and stored first element of string.
        last_digit = int(value_n[-1])    # accessed and stored last element of string.
        sum_is = (first_digit + last_digit)    # calculating sum.
        break    # to break infinite loop.
    else:
        value_n = input('Enter a number is not starting with 0 : ')    # again prompt if not entered. 
        length_of_value_n = len(value_n)    # calculating length of entered string.

print('First digit : ',first_digit)    # printing first digit.
print('Last digit : ',last_digit)     # printing second digit.
print('Sum of first and last digit : ',sum_is)     # printing sum.