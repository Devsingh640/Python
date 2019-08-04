# This proram is to find frequency of a digit in given number.
print('This proram is to find frequency of a digit in given number.') 

string_is = input('Enter your string here : ')    # taking input string.
frequency = 0;
string_length = len(string_is)    # calculating length of the string.
digit_set = set()    # created an empty set.

for x in range(0, string_length):
    a = string_is[x]    # storing element of string in a using index.
    
    if(a not in digit_set):    # if a is not preset in set.
        for z in range (0, string_length):
            if(a == string_is[z]):    # checking if selected element is equal to all elements.
                frequency = frequency + 1  # incriment frequency by one.
                digit_set.add(a)    # now add the element in set.
            else:
                continue    # else continue the loop.
        print('Frequency of ', a, ' is : ', frequency) # printing frequency of each element.
        frequency = 0 # reset counter.
        