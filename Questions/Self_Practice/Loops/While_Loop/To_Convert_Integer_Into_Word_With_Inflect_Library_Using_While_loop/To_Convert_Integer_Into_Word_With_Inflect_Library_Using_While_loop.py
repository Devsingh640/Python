# This program is to convert a number into words.
import inflect    # importing inflect library.
print('This program is to convert a number into words.')

while True:
    convert_this = int(input('Enter a Number : '))    # taking input from user.
    word = inflect.engine()    #  binding this variable with library.
    print(word.number_to_words(convert_this))    # printing result.