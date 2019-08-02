print('Lets us assume that total no of days in an year are 365.')
print('Lets us assume that a month contains 30 days.')
print('Keeping in mind for now the we can discard the decimal value.')

number1 = int(input('Enter total number of days :'))    #  365 is stored in number1  

print(' ')  # this will print a blank line.
print(' ')  # this will print a blank line.

number2 = int((number1)/365)   # 1 is stored in number2.
number3 = int((number1)/7)   # 52 is stored in number3.
number4 = int(number1)  # 365 is stored in number4.

print('Total no of years : ',number2)   # prints number2 value.  
print('Total no of weeks: ',number3)   # prints number3 value.  
print('Total no of days : ',number4)   # prints number4 value.  
