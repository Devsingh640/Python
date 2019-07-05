print("WELCOME TO YOUR BIT COIN TRANSFER PORTAL")	#Welcome message to portal.

def block_chain_print():	#Print function for list.
	print(block_chain)	#This will be called to print the block list.

def adding_value_to_block_chain():	#Append function for list ie to add value to a list.
	block_chain.append([block_chain[-1], tx_value])	#This will be called to append value to a block chain list


block_chain = []	#Initially empty list.

if block_chain == [] :	#Checking weather the list is empty or not, if empty ask for the fist value.
	first_tx_value = int(input("Enter your first tx value ; "))	#Asking for the first value of list.
	block_chain.append(first_tx_value)	#Calling append function to add the user entered value to list. 
	block_chain_print()	#Calling the print function to print list.


tx_value = int(input("Enter your transfer value here : "))	#Asking the for more transfer value:

adding_value_to_block_chain()	#Calling append function to add the user entered value to list. 

block_chain_print()	#Calling the print function to print list.