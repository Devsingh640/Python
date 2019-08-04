# To find sum of a n natural number using for loop.
print('To find sum of a n natural number using for loop.')

value_n = int(input('Enter a number : '))
power = int(input('Enter a power to be calculated : '))

cal_power = 1 # default result is set to one

for x in range(1, (power + 1)):
    cal_power = cal_power * value_n    # power logic.
    
print(cal_power)    # printing calculated result.