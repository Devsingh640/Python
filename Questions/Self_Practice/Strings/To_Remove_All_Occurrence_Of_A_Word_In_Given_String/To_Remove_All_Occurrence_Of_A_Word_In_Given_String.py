print('To remove all occurrence of a word in given string.')
print(' ')

string_is = input('Enter a string : ')

remove_this = input('Enter a word : ')

string_is = string_is.replace(remove_this, '')

print(string_is)