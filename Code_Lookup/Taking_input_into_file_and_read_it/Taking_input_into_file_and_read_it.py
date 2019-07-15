print("I hope your are fine lets start")	#This is will print the string or variable value on screen.

username = input('Hello user please enter your UserName here: ')	#Taking input from user and storing it to a variable called username.
password = input('Hello user please enter your Password here: ')	#Taking input from user and storing it to a variable called password.
print ("Welcome to your Password file ", username )	#This will print a welcome text followed by variable value.

file = open("profile.html", mode = "w")	#This will first create a file if file not present and opens it in write mode.
file.write(username)	#This will write username value into the file.
file.write(password)	#This will write password value into the file.
file.close()	#This will close the opened file.

file = open("profile.html", mode = "r")	#This will open the required file in read mode.
print(file.read())		#This will read the file out.
file.close()	#This will close the opened file.


