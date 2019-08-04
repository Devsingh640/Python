# This proram is to find if given string is palindrome or not.
print('This proram is to find if given string is palindrome or not.') 

string_is = input('Enter your string here : ')    # taking input string.

string_length = len(string_is)    # calculating length of the string.
counter = 0    # counter value initially set to 0.


if ((string_length % 2 == 0) or (string_length / 2)):    # to check if length is even or odd.
    full = string_length    # full length goes in here.
    half = int((string_length / 2))    # calculating half of the string.
    
    for pointer in range(0, half):
        full = full - 1    # decrementing full by one.
        if ((string_is[pointer]) == (string_is[full])):    # palindrome check.
            counter = counter + 1    # counter value increased by 1.
        else:
            break    # if even a pair is not same then break loop.
        
if (counter >= (half)):
    print("Yes string is palindrome")
else:
    print("No string is not palindrome")