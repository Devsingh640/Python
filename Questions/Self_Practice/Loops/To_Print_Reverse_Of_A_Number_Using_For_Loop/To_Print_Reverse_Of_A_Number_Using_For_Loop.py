#This is a program to print reverse of a number using a for loop.
print('This is a program to print reverse of a number using a for loop.')
input_num = input('Enter a number : ')
print(' ')    # printing blank line.

new_num = ''    # declared a string type variable.
value_n = int(input_num)    # converted string to integer.
length_of_value_n = len(input_num)    # calculating length of string.

for x in range(0, length_of_value_n):
    a = str(value_n % 10)    #remainder goes in a.
    value_n =  int(value_n / 10)    # division result gets converted into int an dagain stored into same variable.
    new_num = new_num + a    # string formation.


new_num = int(new_num)    # string converted to int type.

print('You entered this : ',input_num)    # printing orignal number.
print('Reverse of your number : ',int(new_num))    # printing reversed number.