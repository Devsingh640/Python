# To find factorial of a number using for loop.
print('To find factorial of a number using for loop.')

value_n = int(input('Enter whose factorial needs to be calculated : '))

fact = 1    # initial value of fact.

for x in range(1, (value_n + 1)):
    fact = fact * x    # factorial logic.
    
print(fact)    # printing factoriual reault.