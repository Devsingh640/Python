# To find sum of a n natural number using for loop.
print('To find sum of a n natural number using for loop.')

value_n = int(input('Enter a number : '))

sum_is = 0    # initial value of sum_is.

for x in range(1, (value_n + 1)):
    sum_is = sum_is + x    # sum logic.
    
print(sum_is)    # printing sum result.