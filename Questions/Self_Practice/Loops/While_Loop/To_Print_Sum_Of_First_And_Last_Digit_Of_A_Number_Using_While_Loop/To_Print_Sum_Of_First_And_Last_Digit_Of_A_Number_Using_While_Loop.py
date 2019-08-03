#This is a program to swap first and last digit of a number using a while loop.
print('This is a program to swap first and last digit of a number using a while loop.')
value_n = input('Enter a number : ')
length_of_value_n = len(value_n)    # calculating length of entered string.

while True:    # infinite loop. 
    if(length_of_value_n > 0):    # if something is entered then execute.
        first_digit = int(value_n[0])    # converted first element of string into int.
        last_digit = int(value_n[-1])    # converted last element of string into int.
        sum_is = (first_digit + last_digit)    # calculating sum. 
        break    # to break infinite loop.
    else:
        value_n = input('Enter a number : ')    # again prompt if not entered. 
        length_of_value_n = len(value_n)    # calculating length of entered string.

print('First digit : ',first_digit)    # printing first digit.
print('Last digit : ',last_digit)     # printing second digit.
print('Sum of first and last digit : ',sum_is)     # printing sum.