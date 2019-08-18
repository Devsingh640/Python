print('To Remove First Occurrence of a Character in a String.')
 
string_is = input("Enter a string : ")
character = input("Enter a character : ")

new_string = ''
length = len(string_is)
i = 0

while(i < length):
    if(string_is[i] == character):
        new_string = string_is[0 : i] + string_is[i + 1 : length]
        break
    i = i + 1
 
print("Original String :  ", string_is)
print("Final String :     ", new_string)

