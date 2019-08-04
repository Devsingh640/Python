# This program is to print all ascii characters.
print('This program is to print all ascii characters.')

for x in range(0, 128):
    ascii_character = chr(x)    # converting integer to ascii character,
    print('ASCII character for code ', x, ' is : ',ascii_character)    # printing character.