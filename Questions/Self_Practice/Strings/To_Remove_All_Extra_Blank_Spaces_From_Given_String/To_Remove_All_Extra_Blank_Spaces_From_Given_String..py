print('To remove all extra blank spaces from given string.')
string_is = input('Enter a string : ')
new_string = ''
string_length = len(string_is)
previous_element = 32

for index in range(0, string_length):
    
    index_element = string_is[index]
    element_ascii_value = ord(index_element)
    
    if((element_ascii_value == 32) and (element_ascii_value == previous_element)):
        pass
    else:
        new_string = new_string + string_is[index]
    
    previous_element = element_ascii_value   
    
print(new_string)