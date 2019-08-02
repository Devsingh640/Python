#This is a program to print all alphabet from a to z using while loop.
print('This is a program to print all alphabets from a to z ')
alphabet_a = 97 # Stores ascii value of a in alphabet_a.
alphabet_z = 122  ## Stores ascii value of a in alphabet_z.
x = alphabet_a  # setting counter to alphabet_a. 
while x < alphabet_z:  # while loop runs till x value is less then alphabet_z. 
    x = x + 1   # counter value incrimented by one here.
    a = chr(x)  #converted the integer value in x to character.
    print(a)    # printing a.        
